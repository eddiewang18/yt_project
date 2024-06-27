from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from utils.utils import download_and_convert_youtube_video
import os
from django.http import FileResponse
from django.utils.encoding import escape_uri_path
import configparser
from django.conf import settings
from .youtube import YoutubeData
from .models import Yt_Stat,Yt_Stat_tags
from account.models import MyUser

class HomeView(APIView):
    
    def get(self,request):
        response_yt_data = {
            "TW":[],
            "US":[],
            "JP":[],
            "KR":[]
        }
        # 使用 BASE_DIR
        base_dir = settings.BASE_DIR
        api_key_google = configparser.RawConfigParser()
        api_key_google.read(base_dir/'google.ini')
        api_key = api_key_google['google']['api_key'] # google api key
        yt = YoutubeData(api_key)
        for k in response_yt_data:
            if yt.getHitVideo(k,'10',8) != None :
                response_yt_data[k]= yt.getHitVideo(k,'10',8)
        return Response(response_yt_data)

    def post(self, request):
        # youtube音檔轉換
        try:
            data = request.data
            yt_link = data.get('yt_link')
            filetype = data.get('fileType')
            email = data.get("email")

            if not yt_link or not yt_link.strip():
                return Response({"error": "Youtube連結不可空白"}, status=status.HTTP_400_BAD_REQUEST)

            if filetype not in ["mp3", "mp4"]:
                return Response({"error": f"未支援{filetype}類型的轉換"}, status=status.HTTP_400_BAD_REQUEST)

            result = download_and_convert_youtube_video(yt_link, filetype) # 轉檔
            if result:
                response = FileResponse(file_iterator(result))
                file_name = f"download.{filetype}"
                response['Content-Disposition'] = f'attachment; filename="{file_name}"'
                response['Content-Type'] = 'application/octet-stream'

                # 儲存數據
                base_dir = settings.BASE_DIR
                api_key_google = configparser.RawConfigParser()
                api_key_google.read(base_dir/'google.ini')
                api_key = api_key_google['google']['api_key'] # google api key
                yt = YoutubeData(api_key)
                yt_data_result = yt.get_video_data(yt_link)
                if yt_data_result :
                    yt_title = yt_data_result['yt_title']
                    tags = yt_data_result['tags']
                    img_url = yt_data_result['img_url']
                    save_data = {
                        "yt_url":yt_link,
                        "convert_type":filetype,
                        "img_url":img_url,
                        "yt_title":yt_title
                    }
                    if email:
                        user = MyUser.objects.get(email=email)
                        save_data['cuser'] = user
                    yt_stat_instance = Yt_Stat.objects.create(**save_data)
                    if tags:
                        for tag in tags:
                            Yt_Stat_tags.objects.create(stat_id = yt_stat_instance,tag_name = tag)
                return response
            else:
                # print("檔案不存在")
                return Response({"error": "檔案不存在"}, status=status.HTTP_404_NOT_FOUND)

            return Response({"status": "OK"})
        
        except Exception as e:
            print(f"Error=>{e}")
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# 用於分塊讀取文件內容並在讀取完成後刪除文件
def file_iterator(file_name, chunk_size=512):
    with open(file_name, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk
    # 删除文件
    os.remove(file_name)


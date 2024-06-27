from googleapiclient.discovery import build
import re

class YoutubeData():
    regionCode = ('US','CA','JP','KR','TW','CN','GB','DR','FR','AU','IN','RU','TW')
    videoCategoryId = ('10','20','17','25','24')
    '''
        音樂：10
        遊戲：20
        體育：17
        新聞：25
        娛樂：24
    '''
    def __init__(self,api_key):
        self.youtube = build('youtube', 'v3', developerKey=api_key)
        

    def getHitVideo(self,regionCode:str,videoCategoryId:str,maxResults:int) -> list :
        if regionCode not in YoutubeData.regionCode:
            return None 
        if videoCategoryId not in YoutubeData.videoCategoryId:
            return None 
        result = []
        request = self.youtube.videos().list(
            part='snippet,contentDetails,statistics',
            chart='mostPopular',
            regionCode= regionCode,  
            videoCategoryId=videoCategoryId, 
            maxResults=maxResults
        )

        response = request.execute()

        for item in response['items']:
            thumbnails = item['snippet']['thumbnails']
            result.append(
                {
                    'title':item['snippet']['title'],
                    'video_id':item['id'],
                    'video_url':  f'https://www.youtube.com/watch?v={item["id"]}',
                    'img':thumbnails.get('maxres', {}).get('url')
                }
            )
        return result

    def get_video_id(youtube_url):
    # 使用正则表达式提取视频 ID
        pattern = r'(?:v=|\/)([0-9A-Za-z_-]{11}).*'
        match = re.search(pattern, youtube_url)
        return match.group(1) if match else None 

    def get_video_data(self,youtube_url):
        video_id = YoutubeData.get_video_id(youtube_url)
        if video_id:
            # 获取视频的相关信息
            request = self.youtube.videos().list(
                part='snippet,contentDetails,statistics',
                id=video_id
            )
            response = request.execute()

            # 打印视频信息
            if response['items']:
                video = response['items'][0]
                title = video['snippet']['title']
                description = video['snippet']['description']
                tags = video['snippet'].get('tags', [])
                thumbnails = video['snippet']['thumbnails']
                
                # 获取不同尺寸的缩略图 URL
                # default_thumbnail = thumbnails.get('default', {}).get('url')
                # medium_thumbnail = thumbnails.get('medium', {}).get('url')
                high_thumbnail = thumbnails.get('high', {}).get('url')
                # print("\n訊息:")
                # print(f'Title: {title}')
                # print(f'Description: {description}')
                # print(f'Tags: {tags}')
                # print(f'Default Thumbnail: {default_thumbnail}')
                # print(f'Medium Thumbnail: {medium_thumbnail}')
                # print(f'High Thumbnail: {high_thumbnail}')
                return {
                    "yt_title":title,
                    "tags":tags,
                    "img_url":high_thumbnail
                }
            else:
                return None
        else:
            return None      
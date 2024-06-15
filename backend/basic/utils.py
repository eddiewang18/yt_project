import os
from pytube import YouTube
from moviepy.editor import VideoFileClip
from datetime import datetime

# youtube 影片轉mp4或mp3


def download_and_convert_youtube_video(video_url, filetype):
    try:
        # 下載YouTube影片
        yt = YouTube(video_url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
        video_filename = stream.download()

        # 根據filetype進行轉換
        if filetype == 'mp4':
            # 如果要下載為mp4，則不需要額外轉換
            print(f'Downloaded video: {video_filename}')
            return video_filename
        elif filetype == 'mp3':
            # 轉換成mp3
            video_clip = VideoFileClip(video_filename)
            audio_clip = video_clip.audio
            audio_filename = video_filename[:-4] + '.mp3'  # 更改檔案副檔名為mp3
            audio_clip.write_audiofile(audio_filename)
            audio_clip.close()
            video_clip.close()
            print(f'Converted to MP3: {audio_filename}')
            
            # 刪除原始的mp4檔案
            os.remove(video_filename)
            print(f'Deleted original MP4: {video_filename}')
            
            return audio_filename
        else:
            print('Unsupported filetype. Supported types: mp4, mp3')
            return None
    except Exception as e:
        print(f'Error: {str(e)}')
        return None

# mp4_or_mp3_machine("https://www.youtube.com/watch?v=zqKoXPHhmsM","mp3","C:\\download_music","rain1")

# 取得今天日期並格式化為 YYYYmmdd 的字串
def getToday():
    return datetime.today().strftime('%Y%m%d')

# 取得目前系統時間並格式化為 hhmmss 的字串
def getTime():
    return datetime.now().strftime('%H%M%S')


from googleapiclient.discovery import build


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


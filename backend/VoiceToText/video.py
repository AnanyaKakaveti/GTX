from pyyoutube import Api, Client
import pytube
from pytube import extract, YouTube

API_KEY = 'AIzaSyBzVZT8C56FTLvWuvOy4-9TJ_YOtD5WKw4'
Suerte = 'https://www.youtube.com/watch?v=a8Rwz6zBJSE'
client = Client(api_key=API_KEY)

suerte_id = pytube.extract.video_id(Suerte)
print(suerte_id)

yt = YouTube(Suerte)


# urlData = "https://www.googleapis.com/youtube/v3/search?key={}&maxResults={}&part=snippet&type=video&q={}".format(
#     API_KEY, count, random)
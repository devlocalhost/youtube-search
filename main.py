import pafy
import requests
import json
from youtubepy import Video

apiKey = 'yourYouTubeAPIkey'

pafy.set_api_key(apiKey)

ask = input(' Search for something: ')
video = Video(ask)

lnk = video.search()
url = lnk

video = pafy.new(url)

vttl = video.title
vauth = video.author
vdr = video.duration
vdsc = video.description
vpbl = video.published
vvie = video.viewcount
vid = video.videoid
vthm = video.thumb
vbthm = video.bigthumbhd

rqs = requests.get(f'https://www.googleapis.com/youtube/v3/videos?id={vid}&key={apiKey}&part=statistics')
res = rqs.json()

disl = (res['items'][0]['statistics']['dislikeCount'])
lik = (res['items'][0]['statistics']['likeCount'])

print('===================================')
print(f' Information about "{vttl}"')
print('===================================')
print(f' Title: {vttl}')
print('===================================')
print(f' Link: {url}')
print('===================================')
print(f' Thumbnail URL: {vthm}')
print('===================================')
print(f' "Larger (HD)" thumbnail URL: {vbthm}')
print('===================================')
print(f' Video ID: {vid}')
print('===================================')
print(f' Uploaded by: {vauth}')
print('===================================')
print(f' At: {vpbl}')
print('===================================')
print(f' Duration: {vdr}')
print('===================================')
print(f' Likes: {lik}')
print('===================================')
print(f' Dislikes: {disl}')
print('===================================')
print(f' Views: {vvie}')
print('===================================')
print(f' Description: \n===================================\n{vdsc}')
print('===================================')

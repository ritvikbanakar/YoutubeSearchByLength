import json
import requests
import os
import youtube_api
from youtube_api import YoutubeDataApi
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

api_key="AIzaSyDCKVodrvehRJjeAETCNn0OjQRU3SAk5jo"
yt = YoutubeDataApi(api_key)
resultNum = 5
searchingFor = input("Enter what you would like to search for: ")
resultNum = int(input("Enter how many results you would like to have: "))

searches = yt.search(q=searchingFor, max_results=resultNum)
for var in list(range(resultNum)):
  searchDict = searches[var]
  video_id=searchDict["video_id"]
  searchUrl="https://www.googleapis.com/youtube/v3/videos?id="+video_id+"&key="+api_key+"&part=contentDetails"
  response = requests.get(searchUrl, verify=False)
  data = json.loads(response.text)
  all_data=data['items']
  contentDetails=all_data[0]['contentDetails']
  duration=contentDetails['duration']
  print( searchDict["video_title"] + " "+ duration)

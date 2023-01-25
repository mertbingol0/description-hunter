"""
Author: mertbingol0
Date: 2023/01/26
Project: description-hunter
"""

import requests
import re

channell_id = input('Please enter Channel ID: ')
url_part_1 = 'https://youtube.googleapis.com/youtube/v3/search?part=snippet&channelId='
url_part_2 = '&maxResults=50&key=***=json' #yildizli olan yere youtube api'nin key'i gelmelidir.
next_page_token = ''

unparsing_url = url_part_1 + channell_id + url_part_2

res = requests.get(unparsing_url)
data = res.json()

links = []
for item in data['items']:
    video_description = item['snippet']['description']
    links += re.findall(r'https?://[-\w./:]+', video_description)
    if 'nextPageToken' in data:
        next_page_token = data['nextPageToken']
    else:
        break

for i, link in enumerate(links):
    print(f"{i+1}. {link}")

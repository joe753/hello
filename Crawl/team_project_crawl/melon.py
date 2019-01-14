from bs4 import BeautifulSoup
import requests
import function
import time
import random
import json


url = "https://www.melon.com/chart/index.htm"

headers = {
    'Host': 'www.melon.com',
    'If-None-Match' : "0:b170",
    'Referer': 'https://www.melon.com/index.htm',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

html = requests.get(url, headers = headers).text






like_id = []
likecnt = []
song_no = []

rank = []
song_name = []
singer = []

    

soup = BeautifulSoup(html, 'html.parser')
sel_song = "#frm table tbody tr "


b = 0
get_song = soup.select(sel_song)
for i in get_song:
    song_number = i.attrs["data-song-no"]
    song_no.append(song_number)
    rank.append(("[순위] : " + i.select_one('div span.rank').text + "위"))
    song_name.append(("[곡명] : "+ i.select_one('div.rank01 span a').text))
    singer.append(("[가수] : " +i.select_one('div.rank02 span').text))

print ()

url2 = "https://www.melon.com/commonlike/getSongLike.json"
params = {'contsIds': ",".join(song_no)
}
headers = {
        'Accept': '*/*',
       'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
       'Connection': 'keep-alive',
        'Cookie': 'SCOUTER=x6r42imbf7pkvq; PCID=15474271513241870574604; PC_PCID=15474271513241870574604; POC=WP10',
        'Host': 'www.melon.com',
        'Referer': 'https://www.melon.com/chart/index.htm',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequestecko) Chrome/71.0.3578.98 Safari/537.36'
}


html2 = requests.get(url2, headers = headers, params=params).text


 
jsonData = json.loads(html2, encoding='utf-8')


for j in jsonData['contsLike']:
    if str(j['CONTSID']) == str((song_no)[b]):
        likecnt.append(j['SUMMCNT'])
        print (rank[b],"\t" ,song_name[b], '\t' ,singer[b], '\t', ( "[좋아요] : " + str(likecnt[b])))
        b = b+1
    else :
        continue
            
    # b = b + 1
    
# print (like_id)
# print (get_song)

# print (get_url)



   




# for i in get_url :
#     a = i.get('')
#     print (a)



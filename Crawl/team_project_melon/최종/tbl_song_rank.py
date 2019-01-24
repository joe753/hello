from bs4 import BeautifulSoup
import requests
import time
import random
import json
import melon_function as mf
import tbl_album as album
import datetime

# 매일 update되는 Song_Rank Table에 들어갈 data를 가져오는 함수

def song_rank():
    now = datetime.datetime.now()

    like_id = []
    likecnt = []
    song_no = []
    rank = []
    lst = []

    b = 0
    url = "http://vlg.berryservice.net:8099/melon/list"
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    sel = "#frm table tbody tr "

    # song id, rank 가져오기
    get_song = soup.select(sel)
    for i in get_song:
        song_number = i.attrs["data-song-no"]
        song_no.append(song_number)
        rank.append(i.select_one('div span.rank').text)
        

    url2 = "http://vlg.berryservice.net:8099/melon/likejson"
    html2 = requests.get(url2).text
    jsonData = json.loads(html2, encoding='utf-8')

    # 좋아요
    for j in jsonData['contsLike']:
        if str(j['CONTSID']) == str((song_no)[b]):
            likecnt.append(j['SUMMCNT'])
            b = b+1
    
    # update 일자
    date = now.strftime('%Y%m%d')
    for i in range (0,100):
        lst.append([song_no[i], rank[i], date, likecnt[i]])
        print("Rank_lst ----->", (i + 1) , "record  --> done!")
    
    print ("Album_data has been downloaded!!!!")
        

    return (lst)



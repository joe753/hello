from bs4 import BeautifulSoup
import requests
import time
import random
import json
import melon_function as mf
import album
import datetime






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
    sel_song = "#frm table tbody tr "

    get_song = soup.select(sel_song)
    for i in get_song:
        song_number = i.attrs["data-song-no"]
        song_no.append(song_number)
        rank.append(i.select_one('div span.rank').text)
        

    url2 = "http://vlg.berryservice.net:8099/melon/likejson"
    html2 = requests.get(url2).text
    jsonData = json.loads(html2, encoding='utf-8')

    for j in jsonData['contsLike']:
        if str(j['CONTSID']) == str((song_no)[b]):
            likecnt.append(j['SUMMCNT'])
            b = b+1

    date = now.strftime('%Y%m%d')
    for i in range (0,100):
        lst.append([song_no[i], rank[i], date, likecnt[i]])
        print("Rank_lst ----->", (i + 1) , "record  --> done!")
    
    print ("Album_data has been downloaded!!!!")
        

    return (lst)



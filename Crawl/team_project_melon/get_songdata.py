from bs4 import BeautifulSoup
import requests
import time
import random
import json
import melon_function as mf
import album
    


url = "https://www.melon.com/chart/index.htm"
headers = {
    'Referer': 'https://www.melon.com/',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
trs = mf.request(url, headers).select('tbody tr[data-song-no]')

album_lst = album.album_data(trs)

album_insert = "insert ignore into Album (album_id, album_title, album_genre, rating, releasedt, album_comp, entertainment) values (%s, %s, %s, %s, %s, %s, %s) "
mf.save(album_lst, album_insert)


songs = mf.song_data()
mssong_insert = "insert into MS_Song (song_no, title, singer, genre, album_id) values (%s, %s, %s, %s, %s) "
isStart = True
mf.save(songs, mssong_insert)

    
    
    
   



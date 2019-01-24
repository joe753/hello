from bs4 import BeautifulSoup
import requests
import time
import random
import json
import melon_function as mf
import album

def songsinger():
    url = "http://vlg.berryservice.net:8099/melon/list"
    
    sel_song = "#frm table tbody tr "
   
    get_song = mf.request(url).select(sel_song)
   
    lst = []
    
    
    
    for num , i in enumerate(get_song):
        song_number = i.attrs["data-song-no"]
        singer = i.select_one('div.rank02 span').text
        lst.append([song_number,singer])
        # print(album_id)


    conn = mf.get_conn('melondb')
    cursor = conn.cursor()
    sql2 = '''select artist_id, name from Singer'''
    cursor.execute(sql2)
    lines = cursor.fetchall()

    data = []
    for i in lst:
        for j in lines:
            if j[1] in i[1] :
                data.append([j[0],i[0]])
                print ("MS_Song===>>",i,"\nSinger====>>>",j)

    return data



    
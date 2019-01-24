from bs4 import BeautifulSoup
import requests
import time
import random
import json
import melon_function as mf
import album
import re


def singer():
    url = "http://vlg.berryservice.net:8099/melon/list"
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    singers = soup.select('tbody tr[data-song-no] td:nth-of-type(6)  div.ellipsis.rank02 span a')
    singer_info = []

    for singer in singers:
        singer_link = singer.attrs['href']
        singer_name = singer.text
        # print(singer_link)
        pattern = re.compile("\'(.*)\'")
        singer_id = re.findall(pattern, singer_link)[0]
        singer_info.append([singer_id, singer_name])
        print(singer_info)
    return singer_info

singer()



# def singer():
#     url = "http://vlg.berryservice.net:8099/melon/list"
#     html = requests.get(url).text
#     soup = BeautifulSoup(html, 'html.parser')
#     sel_song = "#frm table tbody tr "


#     singer_lst = []
#     get_song = soup.select(sel_song)


#     for i in get_song:
#         a = i.select_one('div.rank02 span').text
#         group = a.split(",")
#         for i in group:
#             singer = i.strip()
#             singer_lst.append(singer)
    
#     print (singer_lst)



   

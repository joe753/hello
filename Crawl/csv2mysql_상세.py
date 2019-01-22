from bs4 import BeautifulSoup
import requests
import csv
import codecs
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
sel_song = "#frm table tbody td div "


b = 0
get_song = soup.select(sel_song)
for i in get_song:
    song_number = i.attrs["data-song-no"]
    song_no.append(song_number)
    rank.append(i.select_one('div span.rank').text)
    song_name.append((i.select_one('div.rank01 span a').text))
    singer.append(i.select_one('div.rank02 span').text)

print ()


###########################################
fp = codecs.open("melon_add_likecnt.csv", "r", encoding="utf-8")
reader = csv.reader(fp, delimiter=',', quotechar='"')


def get_conn(db):
   return pymysql.connect(
       host='localhost',
       user='dooo',
       password='gusdnr75',
       port=3306,
       db=db,
       charset='utf8')

sql_truncate = "truncate table Meltop"
sql_insert = "insert into Meltop (rank, title, singer, likecnt) values (%s, %s, %s, %s) "
isStart = True

def save(lst):
    try:
        conn = get_conn('dooodb')
        conn.autocommit = False
        cur = conn.cursor()
        cur.executemany(sql_insert, lst)
        print("Affected RowCount is", cur.rowcount, "/", len(lst))
        conn.commit()

    except Exception as err:
        conn.rollback()
        print("Error!!", err)

    finally:
        try:
            cur.close()
        except:
            print("Error on close cursor")
        try:
            conn.close()
        except Exception as err2:
            print("Fail to connect!!", err2)

total = len(list(reader))
print (total)


fp2 = codecs.open("melon_add_likecnt.csv", "r", encoding="utf-8")
reader2 = csv.reader(fp2, delimiter=',', quotechar='"')
lst = []
save_unit = 15

for i, row in enumerate(reader2):
    if i != 0 and i != total - 1:
        lst.append((row[0],row[1],row[2],row[3]))

    if len(lst) == save_unit or i == total - 1:
        save(lst)
        lst.clear()





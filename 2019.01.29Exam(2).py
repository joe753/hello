import melon_function as mf
import tbl_album as album
from bs4 import BeautifulSoup
import requests
import time
import pymysql
import re
html = '''
    <dl>
        <dt>국적</dt>
        <dd>대한민국</dd>

        <dt>활동장르</dt>
        <dd>Dance, Ballad, Drama</dd>
    
        <dt>데뷔</dt>
        <dd class="debut_song">
            <span class="ellipsis">
                2016.05.05
                <span class="bar">
                    TTT
                </span>
                <a href="#">TTTTTTTTTTTTT</a>
            </span>
        </dd>
        
        <dt>수상이력</dt>
        <dd class="awarded">
            <span class="ellipsis">
                2018 하이원 서울가요대상
                <span class="bar">|</span>본상
            </span>
        </dd>
    </dl>
'''

soup = BeautifulSoup(html, 'html.parser')

sel = 'dl dt'
dd = 'dl dd'
get_song = soup.select(sel)
get_dd = soup.select(dd)
col_names = {}
dt_lst = []
dd_lst = []
pattern1 = re.compile("(.*)")
b = []
for i in get_song:
    dt_lst.append(i.text)

for num, j in enumerate(get_dd):
    if num == 2 :
        dd_lst.append(j.select_one('span.bar').previous.strip())

    elif num == 3 :
        dd_lst.append([j.select_one('span').next.strip() + j.select_one('span').next.next.text + j.select_one('span').next.next.next.next.strip()][0])
    else : 
        dd_lst.append(j.text)


for i in range(len(dt_lst)):
    col_names[dt_lst[i]] = dd_lst[i]

print (col_names)

prnt_data = '''insert into Singer(nation, genre, debut, award) values (''' + str(col_names['국적']), str(col_names['활동장르']), str(col_names['데뷔']), str(col_names['수상이력']) + ");"
print (prnt_data)




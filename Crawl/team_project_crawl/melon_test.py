from bs4 import BeautifulSoup
import requests
import function
import time
import random
import json

url2 = "https://www.melon.com/commonlike/getSongLike.json?contsIds=31554476%2C31554317%2C31532643%2C31532438%2C31477685%2C31406357%2C31417871%2C31506637%2C31492319%2C31448480%2C31388145%2C31399721%2C31403163%2C30962526%2C31373277%2C31495659%2C31455159%2C31266290%2C31542508%2C31314144%2C31453551%2C31346009%2C31417922%2C31433084%2C31356458%2C31304766%2C31532642%2C31551385%2C31492321%2C31151836%2C31402611%2C31492322%2C31062863%2C31316695%2C31399726%2C31551382%2C31085237%2C31399725%2C31553909%2C31399728%2C31399724%2C30244931%2C31526249%2C31399731%2C31340985%2C31399730%2C31266289%2C31399727%2C31399729%2C31510409%2C31399722%2C30637982%2C31388213%2C31486544%2C30806536%2C31266282%2C30699142%2C3087601%2C31403156%2C31266291%2C31131273%2C31144690%2C30568338%2C31331745%2C31286161%2C31470006%2C31085238%2C31541154%2C31314142%2C31478848%2C31133898%2C31457611%2C30725482%2C31302310%2C30809895%2C31175119%2C30314784%2C8235260%2C31266288%2C30960341%2C31344113%2C30672529%2C31113240%2C31219546%2C30859584%2C30669593%2C31433086%2C31085244%2C31433089%2C31266286%2C30717645%2C31356799%2C31433085%2C30884950%2C31539246%2C31433087%2C31356451%2C31532644%2C30930312%2C31524320%2C31496140"

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

params = {
    'contsIds': '31554476,31554317,31532643,31532438,31477685,31406357,31417871,31506637,31492319,31448480,31388145,31399721,31403163,30962526,31373277,31495659,31455159,31266290,31542508,31314144,31453551,31346009,31417922,31433084,31356458,31304766,31532642,31551385,31492321,31151836,31402611,31492322,31062863,31316695,31399726,31551382,31085237,31399725,31553909,31399728,31399724,30244931,31526249,31399731,31340985,31399730,31266289,31399727,31399729,31510409,31399722,30637982,31388213,31486544,30806536,31266282,30699142,3087601,31403156,31266291,31131273,31144690,30568338,31331745,31286161,31470006,31085238,31541154,31314142,31478848,31133898,31457611,30725482,31302310,30809895,31175119,30314784,8235260,31266288,30960341,31344113,30672529,31113240,31219546,30859584,30669593,31433086,31085244,31433089,31266286,30717645,31356799,31433085,30884950,31539246,31433087,31356451,31532644,30930312,31524320,31496140'
  
}
html2 = requests.get(url2, headers = headers).text

jsonData = json.loads(html2, encoding='utf-8')

for j in jsonData['contsLike'][1:]:
    print(j['SUMMCNT'])

# soup = BeautifulSoup(html, 'html.parser')
# sel_song = "#frm table tbody tr "
# sel_songrank = "#frm table tbody tr div span.rank"
# sel_songname = "#frm table tbody tr div.rank01 span a"


# get_song = soup.select(sel_song)
# # print (get_song)
# get_songrank = soup.select(sel_songrank)
# get_songname = soup.select(sel_songname)

# print (get_song)

# for i in get_song:
#     print (i.select_one('div span.cnt').text)
from bs4 import BeautifulSoup
import requests
# import makeurl
# from pprint import pprint
import time
# url = "http://www.jobkorea.co.kr/Recruit/GI_Read_Comt_Ifrm?Gno=27346931&blnKeepInLink=0&rPageCode=SL"
url = "http://www.jobkorea.co.kr/Recruit/GI_Read_Comt_Ifrm?Gno=27256038&blnKeepInLink=0&rPageCode=SL"
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
a = soup.select('div.artTplInner table')
# print(a)
k = a[0]

# len(head) * len*(tr) = len(td)인 경우
heads = k.select('thead tr th')
h = []
for head in heads:
    hs = head.text
    h.append(hs)  
trs = k.select('tbody tr')
tds = k.select('tbody tr td')
dic = {}
for i in trs:
    data = i.select('td')
    for j in data:
        try : 
            len(j.attrs["rowspan"]) != 0
            row_span = j.attrs["rowspan"]
            print ("TRRYYY \n",j)
    
            time.sleep(3)
        except KeyError:
            print ("EXCEPT \n",row_span)
            time.sleep(3)


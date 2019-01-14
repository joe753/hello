from bs4 import BeautifulSoup
import requests
import function
import time
import random

page_num = 0
b = 0



for h in range(0,160):
    page_num = h + 1

    url = "http://www.jobkorea.co.kr/Recruit/Home/_GI_List/"




    params = {
        'isDefault': 'true',
        'duty': '1000100,1000101,1000102,1000096,1000097',
        'menucode':'',
        'page': str(page_num),
        'pagesize': '50',
        'direct': '0',
        'order': '2',
        'tabindex': '0',
        'fulltime': '0',
        'confirm': '0'
    }
    headers = {
        'Host': 'www.jobkorea.co.kr',
        'Origin' : 'http://www.jobkorea.co.kr',
        'Referer': 'http://www.jobkorea.co.kr/recruit/joblist?menucode=duty',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    html = requests.post(url, params=params, headers = headers).text



    soup = BeautifulSoup(html, 'html.parser')

    sel_comptitle = "div.tplList div.titBx a"
    sel_compname = "div.tplList td.tplCo "    

    get_url = soup.select(sel_comptitle)
    get_name = soup.select(sel_compname)
    
    company_name = []
    url2 = []


    for i in get_url :
        a = i.get('href')
        url2.append("http://www.jobkorea.co.kr" + a)
        # print ("\n\n" , "http://www.jobkorea.co.kr" + a) 



    for j in get_name :
        c = j.select_one('a').text
        company_name.append(c)

    print (company_name)
        # b += 1
        # print (c , b)

#     name_url = []
#     # print (len(url2))
#     for i in range(len(url2)):
#         name_url.append((company_name[i], url2[i]))





#     # 
#     data = soup.select("#dev-gi-list div.titBx a")
#     for i in data:
#         href = i.get('href')
#         # print(href)

#     for k in url2:
#         print (k)
#         b = b + 1
#         function.request_url(k, '#gib_frame')
#         print (k,"=======================>",b, "\n\n")
#         time.sleep(random.randrange(2, 14))

# print (name_url)

# href = data.get('href')
# print (href)
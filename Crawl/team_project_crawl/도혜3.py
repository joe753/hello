from bs4 import BeautifulSoup
import requests
# import makeurl
# from pprint import pprint
import time

with open("./yes.csv", mode = "r", encoding = "utf-8") as yes_file:
    # ids = []
    # compnames = []
    # urls = []
    a = 0
    for line in yes_file:
        compid = line.split(',')[0]
        compname = line.split(',')[1]
        url = line.split(',')[2]
        # print(len(url))
        if a == 0:
            a = a + 1
        #     # print(a)
            continue
        else:
        #     ids.append(compid)
        #     compnames.append(compname)
        #     urls.append(url)
        
 
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
            with open("./sample.csv", mode = "a", encoding = "utf-8") as samp_file:
                if (len(h) * len(trs)) == len(tds):
                    num = len(h)
                    for i in range(num):
                        d = []
                        sel = 'td:nth-of-type({})'.format(i + 1)
                        for tr in trs:
                            tds = tr.select(sel)
                            for td in tds:
                                d_text = td.text
                                d.append(d_text)
                        dic[h[i]] = d
                    # print(dic)
                samp_file.write("{},{},{}\n\n\n".format(compid, compname, dic))
            time.sleep(5)
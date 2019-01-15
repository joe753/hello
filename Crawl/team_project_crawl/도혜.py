from bs4 import BeautifulSoup
import requests
import function
import time
number = []
e = 0
with open ("crawl_iframe.csv", "r", encoding='utf-8') as file_0:
    for line in file_0:
        if line.split(",")[3] == "iFrame_URL" :
            continue
        else:
            e = e+1    
            url = line.split(",")[3]
            html = requests.get(url).text
            soup = BeautifulSoup(html, 'html.parser')
            a = soup.select('div.artTplInner table')
            
           

            if len(a) == 0 :
                b = soup.select('td.detailTable table') 
                print ("============>>>>",e,"<<<<<========== NO =================================", b , "b","\n", "================================ NO ===========>>>>",e,"<<<<<====================== \n",)
                time.sleep(3)

                if len(b) == 0 :
                    c = soup.select('td.detailTable p')
                    print ("=========>>>>",e,"<<<<<============= NO =================================", c,"c", "\n", "================================ NO ========>>>>",e,"<<<<<============ \n")
                    time.sleep(3)
                    continue
                continue
                ### 폭넓은 데이타 = td  좁은 데이타 == artTplInner
            
            k = a[0]

            heads = k.select('thead tr th')
            data = k.select('tbody tr td')
            print ("===========>>>>",e,"<<<<<========== YES ==============================" , heads , data , "\n", "=========================== YES ========>>>>",e,"<<<<<============== \n" )
            time.sleep(3)

            # head = []
            # datum = []
            # with open("detail.csv", "w", encoding='utf-8') as file:
            #     for i in range(len(heads)):
            #         head.append(heads[i].text)
            #     file.write(",".join(head)+"\n")
                
            # with open ("detail.csv", "a", encoding="utf-8") as file2:
            #     for i in range(len(data)):
            #         datum.append(data[i].text)
            #     file2.write(",".join(datum)+"\n")
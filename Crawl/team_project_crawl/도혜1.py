from bs4 import BeautifulSoup
import requests
import function
import time
import datetime
import os

count = 0 
number = []
e = 0
if os.path.exists("count_num.csv") == True:
    with open ("count_num.csv", "r", encoding='utf-8') as count_num:
        for j in count_num:
            cnt = j
    count = int((cnt.split(",")[0]))
    print (count)
    time.sleep(5)    
else :
    count = 0
 
with open("yes.csv", "w", encoding = 'utf-8') as yes_file:
    yes_file.write("{},{},{},{},{}".format("ID", "Company", "iframe_URL", "Time","\n"))
with open ("crawl_iframe.csv", "r", encoding='utf-8') as file_0:
    with open ("count_num.csv", "a", encoding='utf-8') as cnt_file:
        for line in file_0:
            now = datetime.datetime.now()
            if line.split(",")[3] == "iFrame_URL" or int(line.split(",")[0]) <= count:
                continue
            else:
                count += 1    
                cnt_file.write("{},{},{},{}".format(line.split(",")[0], line.split(",")[1], now.strftime('%Y-%m-%d %H:%M:%S'),"\n"))
                url = line.split(",")[3]
                html = requests.get(url).text
                soup = BeautifulSoup(html, 'html.parser')
                a = soup.select('div.artTplInner table')
                
            

                if len(a) == 0 :
                    b = soup.select('td.detailTable table') 
                    print ("============>>>>",count,"<<<<<========== NO =================================", b , "b","\n", "================================ NO ===========>>>>",count,"<<<<<====================== \n",)
                    time.sleep(3)

                    if len(b) == 0 :
                        c = soup.select('td.detailTable p')
                        print ("=========>>>>",count,"<<<<<============= NO =================================", c,"c", "\n", "================================ NO ========>>>>",count,"<<<<<============ \n")
                        time.sleep(3)
                        continue
                    continue
                    ### 폭넓은 데이타 = td  좁은 데이타 == artTplInner
                
                k = a[0]

                heads = k.select('thead tr th')
                data = k.select('tbody tr td')
                with open("yes.csv", "a", encoding = 'utf-8') as yes_add_file:
                    yes_add_file.write("{},{},{},{},{}".format(line.split(",")[0], line.split(",")[1], line.split(",")[3], now.strftime('%Y-%m-%d %H:%M:%S'),"\n"))
                        
                
                print ("===========>>>>",count,"<<<<<========== YES ==============================" , heads , data , "\n", "=========================== YES ========>>>>",count,"<<<<<============== \n" )
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
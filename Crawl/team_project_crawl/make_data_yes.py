from bs4 import BeautifulSoup
import requests
import make_url
import time
import datetime
import os
import random
with open ("yes.csv", "r", encoding='utf-8') as file_0:


    b = []
    c = []
    for line in file_0:
        if line.split(",")[2] == "iframe_URL" :
            continue
        else:
            now = datetime.datetime.now()
            url = line.split(",")[2]
            html = requests.get(url).text
            soup = BeautifulSoup(html, 'html.parser')
            a = soup.select('div.artTplInner table')
            k = a[0]
            kls = []
            vl = []
            company = {}
            dic = {}
            heads = k.select('thead tr th')
            data = k.select('tbody tr td')


            #### Head #####
            for key in heads:
                kls.append(key.text)
                vl.append([])
            
            num = 0
            for value in data:
                if num == len(kls) :
                    num = 0
                    vl[num].append(value.text)
                    num += 1
                else : 
                    vl[num].append(value.text)
                    num += 1

            for i, kl  in enumerate(kls):
                dic[kl] = vl[i]
                company[line.split(",")[1]] = dic

            for i in company:
                print (i, "\n\n\n")
                time.sleep(3)

         

            # #### to make Body ####
            # for body in data:
            #     row = body.select('td')
            #     for j in row:
            #         print (j.text)
            #         time.sleep(3)
            #         c.append(j.text)
                
            #     print (c)
            #     time.sleep(5)
            
            

            # with open("yes.csv", "a", encoding = 'utf-8') as yes_add_file:
            #     yes_add_file.write("{},{},{},{},{}".format(line.split(",")[0], line.split(",")[1], line.split(",")[3], now.strftime('%Y-%m-%d %H:%M:%S'),"\n"))
            #     cnt_file.write("{},{},{},{}".format(line.split(",")[0], line.split(",")[1], now.strftime('%Y-%m-%d %H:%M:%S'),"\n"))
                    
                
            # print ("===========>>>>",line.split(",")[0],"<<<<<========== YES.csv ==============================" , heads , data , "\n", "=========================== YES.csv ========>>>>",line.split(",")[0],"<<<<<y============== \n" )
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
        thead = {}
        
        if line.split(",")[2] == "iframe_URL" :
            continue
        else:
            now = datetime.datetime.now()
            url = line.split(",")[2]
            html = requests.get(url).text
            soup = BeautifulSoup(html, 'html.parser')
            a = soup.select_one('div.artTplInner table')

            if os.path.exists("./yes_folder/"+ line.split(",")[1] + ".xml") == False:
                with open ("./yes_folder/"+ line.split(",")[1] + ".xml", "w", encoding="utf-8" ) as file:
                    file.write("{}".format(a))   
                    print (line.split(",")[1] + ".xml  " + "  has been downloaded.")
                    time.sleep(5)    
            else : 
               
                continue
            time.sleep(5)


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
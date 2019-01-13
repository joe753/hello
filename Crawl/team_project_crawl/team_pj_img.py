from bs4 import BeautifulSoup
import requests
import function
import time
import random



with open("1234.csv", "r", encoding='utf8') as file:
for line in file:
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

for k in url2:
            b = b + 1
            function.request_url(k, '#gib_frame')
            print (k,"=======================>",b, "\n\n")
            time.sleep(random.randrange(2, 14))

###--------------------------------------------------------------------------------------

# for datum in data:
#     datum_res = datum.select('td')
#     a = datum_res[0].text
#     b = datum_res[1].text
#     c = datum_res[2].text
#     print (a,b,c)
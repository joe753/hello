from bs4 import BeautifulSoup
import requests 
import urls

url = "http://www.jobkorea.co.kr/recruit/joblist?menucode=duty&dutyCtgr=10016#anchorGICnt_1"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

sel = "#dev-gi-list a[href]"
   

data = soup.select(sel)
print (data)

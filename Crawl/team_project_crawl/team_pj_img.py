from bs4 import BeautifulSoup
import requests 
import urls

url = "http://www.jobkorea.co.kr/Recruit/GI_Read_Comt_Ifrm?Gno=27357865&blnKeepInLink=0&rPageCode=PL"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

sel = "body.jkNewTemplateVer1 td.detailTable img"
sel2 = "#contentsui_table thead"    

data = soup.select_one(sel)
print (data)
a = data.get('src')
img_src = requests.get(a).content
# data2 = soup.select(sel2)[0].text
# print ("============================data=========\n\n",data2, "\n\n\n", data)
savename = "./images/123.jpg"
with open(savename, mode="wb") as file:
        file.write(img_src)


###--------------------------------------------------------------------------------------

# for datum in data:
#     datum_res = datum.select('td')
#     a = datum_res[0].text
#     b = datum_res[1].text
#     c = datum_res[2].text
#     print (a,b,c)
    
from bs4 import BeautifulSoup
import requests 
import urls

url = "http://www.jobkorea.co.kr/recruit/joblist?menucode=duty&dutyCtgr=10016#anchorGICnt_1"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

sel = "#dev-gi-list a"
# sel2 = "#contentsui_table thead"    

data = soup.select(sel)
b = '/Recruit/GI_Read/'
for i in data :
    a = i.get('href')
    # print (a)
    if b not in a :
        continue
    print ("\n\n" , "http://www.jobkorea.co.kr" + a)
# print (data)
# a = data.get('href')
# print (a)
# img_src = requests.get(a)
# print (img_src)
# data2 = soup.select(sel2)[0].text
# print ("============================data=========\n\n",data2, "\n\n\n", data)


###--------------------------------------------------------------------------------------

# for datum in data:
#     datum_res = datum.select('td')
#     a = datum_res[0].text
#     b = datum_res[1].text
#     c = datum_res[2].text
#     print (a,b,c)
    
# def request_url(site, uri):
#     res = requests.get(site)
#     soup = BeautifulSoup(res.text, 'html.parser')
#     uri = uri
#     url = soup.select(uri)[0]
#     return (url)
   
# def down_img (site):
#     # 제목 CSV파일화
#     res = requests.get(site)
#     soup = BeautifulSoup(res.text, 'html.parser')
#     sel_2 = "div.se-title-text"
#     texts = soup.select(sel_2)[0].text
#     save_name = "2.csv"
#     with open(save_name, mode="w") as file:
#         file.write(texts)
#     #이미지 다운로드
#     sel = "img.se-image-resource"
#     imgs = soup.select(sel) 
#     print (imgs, texts)
#     if len(imgs) < 1:
#         exit()
#     for img in imgs:
#         a = 1
#         src = img.get('src')
#         print("img>>", src)
#         img_src = requests.get(src).content
#         saveFile = "./images/"+ str(a) + ".png"
#         with open(saveFile, mode="wb") as file:
#             file.write(img_src)
#         a = a + 1     


# #--- 크롤
# def crawling (site):
#     crawl_site = "http://www.jobkorea.co.kr" + request_url(site, 'iframe#gib_frame').get('src')
#     print (crawl_site)
    




# crawling ('http://www.jobkorea.co.kr/Recruit/GI_Read/27358112?rPageCode=PL')

# imgs = soup.select(sel)
# print(imgs, len(imgs))

# if len(imgs) < 1:
#     exit()

# a = 1

# for img in imgs:
#     src = img.get('src')
#     print("img>>", src)
#     img_src = requests.get(src).content
#     saveFile = "./images/"+ str(a) + ".png"
#     # print ("--------------------------------", saveFile, img_src)
#     with open(saveFile, mode="wb") as file:
#         file.write(img_src)
#     a = a + 1  
#     # write to file

# # a = 0

# for i in src: 
#     a += 1
#     saveFile = "./images/"+ str(a) + ".png"
#     with open(saveFile, mode="wb") as file:
#         file.wirte(i)

# print("OK!")
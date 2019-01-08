from bs4 import BeautifulSoup
import requests


url = "https://blog.naver.com/PostView.nhn?blogId=korea_diary&logNo=221433346994&redirect=Dlog&widgetTypeCall=true&topReferer=https%3A%2F%2Fwww.naver.com%2F&directAccess=false"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

sel = "img.se-image-resource"

imgs = soup.select(sel)
print(imgs, len(imgs))

if len(imgs) < 1:
    exit()

a = 1

for img in imgs:
    src = img.get('src')
    print("img>>", src)
    img_src = requests.get(src).content
    saveFile = "./images/"+ str(a) + ".png"
    # print ("--------------------------------", saveFile, img_src)
    with open(saveFile, mode="wb") as file:
        file.write(img_src)
    a = a + 1  
    # write to file

# a = 0

# for i in src: 
#     a += 1
#     saveFile = "./images/"+ str(a) + ".png"
#     with open(saveFile, mode="wb") as file:
#         file.wirte(i)

# print("OK!")
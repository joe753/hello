from bs4 import BeautifulSoup
import requests


def request_url(site, uri):
    res = requests.get(site)
    soup = BeautifulSoup(res.text, 'html.parser')
    uri = uri
    url = soup.select(uri)[0]
    return (url)
   
def down_img (site):
    res = requests.get(site)
    soup = BeautifulSoup(res.text, 'html.parser')
    sel_2 = "div.se-title-text"
    texts = soup.select(sel_2)[0].text
    save_name = "2.csv"
    with open(save_name, mode="w") as file:
        file.write(texts)

    sel = "img.se-image-resource"
    imgs = soup.select(sel) 
    print (imgs, texts)
    if len(imgs) < 1:
        exit()

    for img in imgs:
        a = 1
        src = img.get('src')
        print("img>>", src)
        img_src = requests.get(src).content
        saveFile = "./images/"+ str(a) + ".png"
        # print ("--------------------------------", saveFile, img_src)
        with open(saveFile, mode="wb") as file:
            file.write(img_src)
        a = a + 1     



def crawling (site):
    crawl_site = "https://blog.naver.com" + request_url(site, 'iframe#mainFrame').get('src') 
    down_img(crawl_site)
    
    
crawling ('https://blog.naver.com/korea_diary/221433346994')

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
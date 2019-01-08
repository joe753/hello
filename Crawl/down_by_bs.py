from bs4 import BeautifulSoup
import requests

url = "https://www.facebook.com/cookatkorea/videos/2123558291288467/?t=2"
img = requests.get(url).content

saveFile = "./images/aaa.png"
with open(saveFile, mode="wb") as file:
    file.write(img)

print("OK!")

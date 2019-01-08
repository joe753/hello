from bs4 import BeautifulSoup
import requests

url = "https://play.google.com/store/apps/category/GAME/collection/topselling_paid"
res = requests.get(url)  #url = 편지를 주소만 적어준다. res -> 주소를 적어준뒤 그 답장이 온것이 res

soup = BeautifulSoup(res.text, 'html.parser')
card_list = soup.select('div.card-list')
# print (card_list)

print (">>>>>>>>>>", len(card_list), card_list[0].get('class'))
for i in card_list:
    cards = i.select('.card')
    print("LLL>>", len(cards))
    for c in cards:
        title =  c.select('a.title')[0].text
        comp = c.select('a.subtitle')[0].text
        price = c.select('.display-price')[0].text

print (c)
print(">>", c.get('class'), [title, comp, price])
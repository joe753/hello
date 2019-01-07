from bs4 import BeautifulSoup
import requests

class Game:
    title = ''
    def __init__(self, tag):
        self.title = c.select('a.title')[0].text.strip()
        self.comp = c.select('a.subtitle')[0].get('title')

    def get_text(self, parent_tag, selector):
        t = self.get_tag(parent_tag, select)
        return "" if t == None else t.text.strip


    def get_tag(self, parent_tag, selector):
        return parent_tag.select(selector)
        

url = "https://play.google.com/store/apps/category/GAME/collection/topselling_paid"
res = requests.get(url)  #url = 편지를 주소만 적어준다. res -> 주소를 적어준뒤 그 답장이 온것이 res

soup = BeautifulSoup(res.text, 'html.parser')
card_list = soup.select('div.card-list')
# print (card_list)
# print (">>>>>>>>>>", len(card_list), card_list[0].get('class'))


for i in card_list:
    cards = i.select('.card')
    print("LLL>>", len(cards))
    for c in cards:
        title =  c.select('a.title')[0].text
        comp = c.select('a.subtitle')[0].text
        price = c.select('.display-price')[0].text
        print (title,comp,price)
# with open ("lists.csv", "w", encoding='utf-8') as file:
#     for l in titles:
#         file.write(l + "\n")
    

# with open ("lists.csv", "w", encoding='utf-8') as file:
#     for l in lists        

       
        

         
       





# def write_file():
#     with open("a.csv", "w", encoding='utf8') as file:
#         file.write("이름,성별,나이\n")
#         file.write("이현욱,남,26\n")
#         file.write("이현민,남,28\n")

# def read_file():
#         with open("a.csv", "r") as file:
#             for line in file:
#                 print (line)
# write_file()
# read_file()
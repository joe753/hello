import requests
import json
from bs4 import BeautifulSoup
import time
import re
import pymysql
import test_func as tf
from pprint import pprint
from pymongo import MongoClient, DESCENDING


url = "https://openapi.naver.com/v1/search/book.json"

title = "파이썬"
params = {
    "query": title,
    "display": 100,
    "start": 1,
    "sort": "date"
}

headers = {
    "X-Naver-Client-Id": "cvwQE3zC2b3yqOsiCARI",
    "X-Naver-Client-Secret": "LMeJ56dEIu"
}

res = requests.get(url, params = params, headers = headers).text

jsonData = json.loads(res)
items = jsonData['items']

for item in items:
    
    if item['discount'] == '':
        item['discount'] = item['price']
    item['price'] = int(item['price'])
    item['discount'] = int(item['discount'])



# pprint (jsonData['items'])
# pprint (jsonData['price'])


mongo_client = MongoClient('localhost', 27017)
collection = mongo_client.dooodb.Books
collection.delete_many({})
result = collection.insert_many(items)
print('Affected docs is {}'.format(len(result.inserted_ids)))
lst = collection.find().sort('likecnt', DESCENDING).limit(5)


prices = collection.find().sort('price', DESCENDING).limit(10)
for i in prices:
    pprint (i)



  
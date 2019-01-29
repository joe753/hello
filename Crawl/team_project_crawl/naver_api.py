import requests
import json
from bs4 import BeautifulSoup
import time
import re
import pymysql
import test_func as tf


url = "https://openapi.naver.com/v1/search/blog.json"

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


# print(json.dumps(jsonData, ensure_ascii=False, indent=2))
tbl_blogger = []
tbl_blogpost = []
pattern1 = re.compile("com/(.*)")
pattern2 = re.compile("https://(.*)/")
pattern3 = re.compile("(.*)/")
for item in jsonData['items']:
    blogger_id = re.findall(pattern1, item['bloggerlink'])
    if blogger_id == ['']:
        blogger_id = re.findall(pattern1, item['bloggerlink'])[0]
        blogger_link = re.findall(pattern3, item['bloggerlink'])[0]
        tbl_blogger.append([blogger_id ,item['bloggername'], blogger_link])
        tbl_blogpost.append([item['title'].replace('</b>','').replace('<b>','') , item['link'], blogger_id, item['postdate']])
    elif blogger_id == []:
        blogger_id = re.findall(pattern2, item['bloggerlink'])[0]
        blogger_link = re.findall(pattern3, item['bloggerlink'])[0]
        tbl_blogger.append([blogger_id ,item['bloggername'], blogger_link])
        tbl_blogpost.append([item['title'].replace('</b>','').replace('<b>','') , item['link'], blogger_id, item['postdate']])

    else : 
        blogger_id = re.findall(pattern1, item['bloggerlink'])[0]
        tbl_blogger.append([blogger_id ,item['bloggername'],item['bloggerlink']])
        tbl_blogpost.append([item['title'].replace('</b>','').replace('<b>','') , item['link'], blogger_id, item['postdate']])

print (tbl_blogger)

blogger_insert = "insert ignore into Blogger (blogger_id, blogger_name, blogger_link) values (%s, %s, %s)"
blogpost_insert = "insert into BlogPost (blog_title, blog_link, blogger_id,postdate) values (%s, %s, %s, %s)"

tf.save (tbl_blogger, blogger_insert)
tf.save (tbl_blogpost, blogpost_insert)
#     # print(item['title'].replace('</b>','').replace('<b>',''), item['bloggerlink'], item['bloggername'], item['postdate'])






  
from apiclient.discovery import build
from pprint import pprint
import time
from pymongo import MongoClient, DESCENDING
API_KEY = "AIzaSyCrr-otDVQyJ4TTu34UOpm6jO4x4_RHL6s"



def main():
    mongo_client = MongoClient('localhost', 27017)
    collection  = mongo_client.dooodb.pythons
    collection.delete_many({})

    for items in search_youtube('python'):
        save(collection, items)
    
    top10(collection)

def search_youtube(title):

    youtube = build('youtube', 'v3', developerKey=API_KEY)

    req = youtube.search().list(
        part='snippet',
        q=title,
        type='video',
        maxResults=50
    )
    
    i = 0
    while req and i < 2:
        search_res = req.execute()
        ids = []
        results = search_res['items']
        for item in results:
            ids.append( item['id']['videoId'])
        stat_res =  youtube.videos().list(
            part='snippet, statistics',
            id=','.join(ids)
        ).execute()

        yield stat_res['items']
        i = i +1
        req = req = youtube.search().list_next(req, search_res)




def save(collection, items):
    for item in items:
        pprint (item['statistics'])
        item['statistics']['viewCount'] = int(item['statistics']['viewCount'])


   
    result = collection.insert_many(items)  
    print('Affected docs is {}'.format(len(result.inserted_ids)))  


def top10 (collection):
    lst = collection.find().sort('statistics.viewCount', DESCENDING).limit(10)
    for i in lst:
        stat = i['statistics']
        snip = i['snippet']
        print (stat['viewCount'], snip['title'])


if __name__ == '__main__':
    main()




 

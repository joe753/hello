import urllib.request as ur

input_data = input("찾고자하는 날짜를 입력해주세요. \n usage>>>> 2018-01-01, 2018-12-31 \n\n")
date = input_data.split(',')
if len(date) < 2:
    print ("Input data Error!!!")
    exit()
    
a = date[0].strip()
b = date[1].strip()
print (a, b)
url = "http://www.weather.go.kr/weather/earthquake_volcano/domesticlist_download.jsp?startSize=999&endSize=999&pNo=1&startLat=999.0&endLat=999.0&startLon=999.0&endLon=999.0&lat=999.0&lon=999.0&dist=999.0&keyword=&startTm=" + a + "&endTm=" + b + "\""
saveFile = "./images/test5.html"
ur.urlretrieve(url, saveFile)
print("OK!")
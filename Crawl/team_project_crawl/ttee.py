from bs4 import BeautifulSoup
import requests
import function
import time
import random



b = 0
with open("123.csv", "wr", encoding='utf8') as file:
	for line in file:
		# res = requests.get(line.split(",")[1])
		# for k in res:
		# 	print (k)
		b = b + 1
		function.request_url(line.split(",")[1], '#gib_frame')
		print (line.split(",")[1],"=======================>",b, "\n\n")
		time.sleep(random.randrange(2, 14))


	###--------------------------------------------------------------------------------------

	# for datum in data:
	#     datum_res = datum.select('td')
	#     a = datum_res[0].text
	#     b = datum_res[1].text
	#     c = datum_res[2].text
	#     print (a,b,c)
from bs4 import BeautifulSoup
import requests
import function
import time
import random



b = 0
with open ("crawl_site.csv", "r", encoding='utf8') as file:
	with open ("crawl_iframe.csv", "w", encoding='utf8') as file2:
		file2.write("{},{},{},{},{}".format("ID","Company_name", "URL", "iFrame_URL", "\n"))
		for line in file:
			# res = requests.get(line.split(",")[1])	
			# for k in res:
			# 	print (k)
			b = b + 1
			function.request_url(line.split(",")[1], '#gib_frame')
			file2.write("{},{},{},{},{}".format(line.split(",")[0],line.split(",")[2],line.split(",")[1], function.request_url(line.split(",")[1], '#gib_frame'), "\n"))
			print (line.split(",")[1],"=======================>",line.split(",")[0], "\n\n")
			time.sleep(random.randrange(2, 14))
	


	###-----------------------------------------------
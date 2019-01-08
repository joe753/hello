import urllib.request as ur

url = 
saveFile = "./images/weather.html"
mem = ur.urlopen(url).read()
with open(saveFile, mode="wb") as file:
    file.write(mem)

print("OK!")


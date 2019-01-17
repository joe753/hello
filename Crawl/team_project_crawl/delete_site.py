a = []

with open("crawl_site.csv", mode="r", encoding="utf-8") as file: 
    for i in file:
        a.append(i)


with open("crawl_site2.csv", mode="w",  encoding="utf-8") as file2: 
    for i in range(6820):
        file2.write(a[i])


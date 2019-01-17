import csv, codecs
import time

fp = codecs.open("melon_rank.csv", "r", encoding="euc-kr")

# aaa,bbb,"ccc,cc"
reader = csv.reader(fp, delimiter=',', quotechar='"')
h = 0

all_data = []
add_column = []
likecnt = []
like_minus = []

for cells in reader:
    h += 1
    if h == 1 :
        continue
    else :
        all_data.append(cells)
        likecnt.append(int(cells[3]))

likecnt.sort()

for i in all_data:
    i.append(int(i[3]) - likecnt[0])
    add_column.append(i)


print (add_column)
    



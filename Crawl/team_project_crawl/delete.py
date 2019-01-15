import datetime


with open ("count_num.csv", "r", encoding='utf-8') as cnt_file:
    for i in cnt_file:
        i = i
print (i.split(",")[0])
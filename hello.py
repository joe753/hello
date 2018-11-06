i , sum = 0,0
while (i >= 0):
    i += 1
    if (i >= 30 and i < 40):
        continue

    sum += i
    if (i == 100):
        print ("end!!", sum)
        break
        
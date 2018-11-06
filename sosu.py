i, sum = 0,0
while (i < 100):
    i += 1
    if (i % 2 == 0 or 1 % 3 == 0 or i % 5 == 0 or i % 7 == 0):
        continue
        sum += i
print(sum)
a,b = (0,0)
for a in range(101):
    b += a

print(b)


a,b = (0,0)
for a in range (100):
    if (a % 2 == 1):
        b += a
print (b)


sum = 2
for i in range (2 , 101):
    for j in range (2 , i):
        if (i % j == 0):
            break
        if (j == (i-1)):
            sum += i


print (sum)

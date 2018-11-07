sum = 0
for n in range(2, 101):
    print (n)
    if (n == 2):
        sum += 2
        continue
    for m in range(2, n):
        if (n % m == 0): #나누어 지면 소수가 아님
            break        # 다음 번호를 검색
        if (m == n - 1): #  n은 소수이다.
            sum += n         
           
print(sum)
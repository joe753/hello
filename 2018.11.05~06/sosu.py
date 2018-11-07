for n in range (2,101):
    for sum in range(1,101):
        if (sum <= n):
            continue
        re = n / sum
        if (re // sum == 1):
            continue
        if (n % sum == 0 and re >= 1 ):        
            print(re)
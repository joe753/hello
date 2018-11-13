numbers = [5,3,4,2,1]
strs = ["aaa", "ccc", "ddd", "asfds", "한글", "영어", "국어", "소소한"]
sort_numbers = sorted(numbers) #오름차순   /////  # 내림차순 reversed(numbers) 
print("sort_numbers=", sort_numbers)
print("numbers=", numbers)


numbers.sort()
print("asc>>", numbers)

numbers.sort(reverse=True)
print("desc>>", numbers)

sort_strs = sorted(strs)
print ("strs>>>", sort_strs)


f = filter(lambda x: x[0] == '한' , strs)
print (list(f))

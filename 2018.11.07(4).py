주소 = input("input(usage: 아이디,비밀번호,이메일주소)>>")
print(주소)
error = "정확히 입력해 주세요."
if 주소 == '':
    print (error)
    exit()

elif (',' not in 주소):
    print (error)
    exit()

message = ("고객님의 아이디는 {} \n비밀번호는 {} \n이메일주소는 {}입니다.")
주소들 = 주소.split(',')

if (len(주소들) != 3):
    print (error)
    exit()
else :
    print (message.format(주소들[0], 주소들[1], 주소들[2]))

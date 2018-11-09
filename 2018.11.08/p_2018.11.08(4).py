cmd = input("원하시는 메뉴와 사이즈를 선택해주세요. \nusage) 아메리카노, grande) \n>>>")
print (cmd)
t = 0
price = [2700, 3000, 3300, 3500, 4000]

outmsg = "주문하신 음료는 {}, 사이즈는 {} 가격은 {}입니다."
a, b, c, d, e = ('아메리카노', '카페라떼', '카푸치노', '바나나라떼', '카페모카')

if (cmd == ''):
    print ('error!!')
    exit()


cmds = cmd.split(',')
if (cmds[0] != a and cmds[0] != b and cmds[0] != c and cmds[0] != d and cmds[0] != e): 
    print ('error!!')
    exit()



if (cmds[0] == a):
    t = price[0]

elif (cmds[0] == b):
    t = price[1]

elif (cmds[0] == c):
    t = price[2]

elif (cmds[0] == d):
    t = price[3]

elif (cmds[0] == e):
    t = price[4]

if (cmds[1] == 'grande' or ' grande'):
    t = t + 500

    

print (outmsg.format(cmds[0], cmds[1], t))


cmd = input("원하시는 메뉴와 가격, 사이즈를 선택해주세요. \nusage) 아이스아메리카노, 3000, grande) \n>>>")
print (cmd)

outmsg = "주문하신 음료는 {}, 가격은 {} 사이즈는 {}입니다."

cmds = cmd.split(',')
print (outmsg.format(cmds[0], cmds[1], cmds[2]))

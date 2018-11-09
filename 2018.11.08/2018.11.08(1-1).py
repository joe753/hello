
while (True) :
    def plus (a, b):
        return a + b

    def minus (a, b):
        return a - b

    def mul (a, b):
        return a * b

    def div (a, b):
        if (b == 0):
            return a

        return a / b
    
    cmd = input("수식을 입력하세요.(usage: 2 + 3)> ")
    cmds = cmd.split(' ')
    
    if (cmds[0] == 'q'):
        quit = input ("계산기를 종료하시겠습니까? (Y or N)\n")

        if (quit == 'Y' or 'y'):
            break
        elif (quit == 'N' or 'n'): 
            continue
         

    a, op, b = cmds
    a, b = int(a), int(b)
    

   
    if (op == '+'):
        r = plus(a, b)
    elif (op == '-'):
        r = minus(a, b)
    elif (op == '*'):
        r = mul(a, b)
    else: 
        r = div(a, b)

    if (op == '/'):
        print ("Answer is {:.3f}".format(r))
    else:
        print ("Answer is {:d}".format(r))

    
        
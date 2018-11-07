def plus(a, b):
    return (a + b)

def minus(a, b):
    return a - b

def divided(a, b):
    return a / b

def multi(a, b):
    return a * b

cmd = input ("사칙연산을 사용하여 계산하시오.(usage : 1 + 2 )")
cmds = cmd.split(" ")

if (not cmds[0].isnumeric() or not cmds[2].isnumeric()):
    print ("숫자를 입력해 주세요.")
    exit()

a = int(cmds[0])
b = int(cmds[2])
op = cmds[1]

if (op == '+'):
    result = plus(a, b)
elif (op == '-'):
    result = minus(a, b)
elif (op == '/'):
    result = divided(a, b)
elif (op == '*'):
    result = multi(a, b)
else :
    print ("Error!!")
    exit()


print (result)
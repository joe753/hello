class Pyung():
    def __init__(self, name):
        self.name = name
    
    def multi(self, a, b):
        return a * b
    
class Jick(Pyung):
    a = 0
    
class Jung(Jick):
    def square(self, a):
        return a * a
    
pyung = Pyung("pyung")
jick = Jick("jick")
jung = Jung("jung")

cmd = input ("구하고자 하는 도형을 고르시오.\n1.평행사변형\n2.직사각형\n3.정사각형\n")
if (cmd in '1'):
    cmd_1 = input ("평행사변형의 밑변과 높이를 입력하세요. (usage >>20, 30)")
    result = cmd_1.split(',')

elif (cmd in '2'):
    cmd_1 = input ("직사각형의 가로와 세로를 입력하세요. (usage >>20, 30)")
    result = cmd_1.split(',')

elif (cmd in '3'):
    cmd_1 = input ("정사각형의 한 변의 길이를 입력하세요. (usage >>20)")

a = int(result[0])
b = int(result[1])

if (result in ','):
    print (jung.multi(a, b))
elif (result not in ','):
    print (jung.square(a))

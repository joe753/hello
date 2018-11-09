class Casting :
    def to_int(s):
        if type(s) == str:
            return int(s)
        else:
            return s

class Pyung():
    a ,b = 0,0
    def __init__(self, name):
        self.name = name
    
    def result(self, a, b):
        return a * b
     
    def say (self,cmd):
        self.answer = input (cmd)
            
    def line (self, msg):
        res = input (msg)
        a, b = res.split(',')
        a, b = int(a), int(b)
        return pyung.result(a, b)

        
class Jick(Pyung):
    
    def __init__(self, name):
        self.name = name

    
class Jung(Jick):
    msg = "정사각형의 한 변의 길이를 입력하세요. (usage >>20)"


pyung = Pyung("pyung")
jick = Jick("jick")
jung = Jung("jung")
msg = "밑변의 길이와 높이를 입력하세요. (usage >>20, 30)"
cmd = "구하고자 하는 도형을 고르시오.\n1.평행사변형\n2.직사각형\n3.정사각형\n"
print (pyung.say(cmd))
print (pyung.line(msg))
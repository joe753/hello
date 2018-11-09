class Pyung:
    def __init__ (self, name):
        self.name = name
    
    def length (self, a, b):
        a,b = int(a), int(b)
        return (a * b)
        

class Rec(Pyung):
    a = 0

class Jung(Rec):
    na = 23
    def line (self, a):
        a =int(a)
        return (a*a)

pyung = Pyung("pyung")
rec = Rec("rec")
jung = Jung("jung")



while (True) :
    cmd = input ("사각형의 종류는??? \n1.평행사변형\n2.직사각형\n3.정사각형\n>>>")
    if (cmd in '1'):
        pyung_result = input ("가로와 높이의 값은? (usage>>> 20, 30)\n >>>")
        pyung_results = pyung_result.split(',')
        print (pyung.length(pyung_results[0],pyung_results[1]))
        break
    elif (cmd in '2'):
        rec_result = input ("가로와 세로의 값은? (usage>>> 20, 30)\n >>>")
        rec_results = rec_result.split(',')
        print (rec.length(rec_results[0],rec_results[1]))
        break
    elif (cmd in '3'):
        jung_result = input ("한 변의 길이는? (usage>>> 20)\n >>>")
        print (jung.line(jung_result))
        break
    else :
        print ("Error!!!!")
        continue


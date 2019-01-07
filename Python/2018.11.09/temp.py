class Casting :
    def to_int(s):
        if type(s) == str:
            return int(s)
        else:
            return s

class 사각형:
    x, y = 0, 0
    name = "사각형"
    def __init__(self):
        print("사각형 created")
    
    # def set_msg(self, msg):
    #     self.msg = msg

    def input_data(self, msg):
        datum = input(msg)
        data = datum.split(',')
        self.x = Casting.to_int(data[0])
        self.y = Casting.to_int(data[1])
        self.넓이(self.x, self.y)


    def 넓이(self):
        return self.x * self.y

class 직사각형(사각형):
    name = "직사각형"
    def 넓이(self, x, y):
        return Casting.to_int(x) * Casting.to_int(y)
    
class 평행사변형(사각형):
    name = "평행사변형"
    def 넓이(self, x, y):
        return Casting.to_int(x) * Casting.to_int(y)

while True:
    print("------------------------------")
    all_rects = [직사각형(), 평행사변형()]
    rect_type = input("\n사각형의 종류는? \n 1) 직사각형\n 2) 평행사변형\n (quit: q) >> ")
    if (rect_type == 'q'):
        break
    
    rect = all_rects[Casting.to_int(rect_type) - 1]
    rect.input_data ("가로와 세로는?? (usage: 가로, 세로)")
    result = rect.넓이(x, y)
    print (name.input_data())
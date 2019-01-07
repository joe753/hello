class Casting:
    def to_int(s):
        if type(s) == str:
            return int(s.strip())
        
        else :
            return s

class 성인:
    name = "성인"
    msg = "사용하실 시간을 숫자만 입력하시오. (usage: 2시간 30분 = 2, 30 (10분단위로 적용)).\n>>>"
    yes_or_no = "맞으시면 (Y) 잘못입력하셨으면 (N)을 눌러주세요."
    
    
    def __init__ (self):
        print ("주문을 시작합니다.")

    def input_1st (self):
        _1st_inputs = input (self.msg)
        _1st_input = _1st_inputs.split(',')
        x, y = Casting.to_int(_1st_input[0]), Casting.to_int(_1st_input[1]) 
        if len(_1st_input) < 2:
            x = 0
        
        self.time(x, y)

    def time (self, x, y):
        time = (x * 60) + y
        y_result = input (self.yes_or_no)
        if y_result != 'y':
            print ("Error!!!!!")
            exit()
        
        self.price(time)    

    def price (self, time):
        price = (time / 10) * 300
        print ("충전하실 시간은 <{}>분, 결제하실 금액은 <{:.0f}>원입니다.\n요금을 넣어주세요.".format(time,price))
        

class 청소년(성인):
    name = "청소년"
    def price(self, time):
        price = (time / 10) * 300 * 0.75
        print ("충전하실 시간은 <{}>분, 결제하실 금액은 <{:.0f}>원입니다.\n요금을 넣어주세요.".format(time,price))
        
class 어린이(성인):
    name = "어린이"
    def price(self, time):
        price = (time / 10) * 300 * 0.5
        print ("충전하실 시간은 <{}>분, 결제하실 금액은 <{:.0f}>원입니다.\n요금을 넣어주세요.".format(time,price))


all_people = [성인(), 청소년(), 어린이()]
first_msg = "당신의 연령대를 선택해주세요."

for i, r in enumerate(all_people):
    first_msg += "\n{:d}) {}\n".format(i + 1, r.name)
       

while True:
    print("==================================================")
    type_people = input(first_msg)
    if (type_people == 'q'):
        break
    
    person_index = Casting.to_int(type_people)
    person = all_people[person_index - 1]
    person.input_1st()









    



 

        
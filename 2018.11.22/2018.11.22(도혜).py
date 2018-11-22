import random


class Deck:                                       ##instance 없이 쓰는 static method로 Deck.make_deck()
    
    deck = []
    received_card = []          ##### received카드를 아래===line 34가 아닌 Deck의 변수로 잡을경우
    def __init__(self):         #####player.pop_card의 received카드와 dealer.popcard의 received카드가 
        print ("good")          ##### 같아지기 때문에 그렇게 만들면 pop된 카드가 4개가 추가될 뿐더러 공유가됨 /// Chris
    
    def make_deck(self):                               ## deck 을 만든다

        shape = ["S","D","H","C"]
        number = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        for i in range (0,4):
            res_shape = shape[i]
            for n in range (0, 13):
                res_number = number[n]

                card = res_shape + res_number
                
                self.deck.append(card)
        return self.deck
        
        
    def shuffle(self):
        
        new = self.deck   ##### self.deck이 아닌 self.make_deck() 함수를 실행해줘야함  /// Chris
        random.shuffle(new)
        return new

    
    def pop_card(self):
        new1 = self.shuffle()
        for i in range(1,3):
            card = new1.pop(i)
            self.received_card.append(card)
        return self.received_card, new1
    
    def hit(self, received, new1):
                 ## hit 하는거                
        received.append(new1.pop(0))
        return received

class Sum:    
    score = []
    num = []
    def jqk_decision(self,f):
        for i in f:
            if 'J' or 'Q' or 'K' in i[1]:
                self.score.append(i[1:])
            
            else :
                self.score.append(i[1:])
            
        print (self.score)

    # def machine_hit(self):

    #     if Sum.make_score <= 17:
    #         self.hit()
    #     elif Sum.sum_result > 17:
    #         return dealer.received_card 
    
    sum_result = 0   
   
    def to_int(self):

        if 'A' in self.score:
            a_choice = input("A는 어떤 값으로 선택하시겠습니까? 1) 1 2) 11>> ")
        
        for i in self.score:
            if 'J' == i or 'Q' == i or 'K' == i:        ##### line 49로 옮기는게 낫지않을까? /// Chris
                i = 10                                      # reason why => def jqk_dec ()의 if 의미가없고 i[1:]로
                self.num.append(i)                          # 다 넣어버리면 될듯
            elif 'A' == i and a_choice == "1":
                i = 1
                self.num.append(i)
            elif 'A' == i and a_choice == "11":
                i = 11
                self.num.append(i)
            else :
                s = int(i)
                self.num.append(s)
        
        print(self.num)

        
    def make_score(self):

            print(sum(self.num))



while True :
    invite = input('게임에 참석하시겠습니까? (Yes / No)'+'\n')       ## 시작

    if invite == 'Yes' :

        player = Deck()
        dealer = Deck()
        finish = Sum()

        a = player.pop_card()
        b = dealer.pop_card()
        
        print("P>>>", a[0])
        print("D>>>", b[0])
        
    elif invite == 'No':
        print('>>>>>>>>>>>','다음에 만나요')
        break

    else :
        print("=============================================Error!!! 다시 입력해주세요.===============================")
        continue
    
    while True:                                                ## 둘째 턴 ~ 종료
        
        gesture = input('카드를 한장 받으시겠습니까? (Yes / No)' + '\n')

        if gesture == 'Yes':
            
            f = player.hit(a[0],a[1])

            print("P>>>", f)
            finish.jqk_decision(f)
            finish.to_int()
            finish.make_score()
           
        elif gesture == 'No':
            
            print("어쩌지")
            # No 하면 여기서 비교해서 승부 보기    ##### No 를 했을 때 finish.make_score 함수를 사용해주는게 어떨지 ///Chris
        
        else :
            print ("Error!!!!!! 다시입력해주세요.")
            continue

        

        

        # #자동 덱받기   >>> 오늘해야할일 중 카테고리 1번
        # def dealer_add_deck ():
        #     while True:
        #         if sum(self.dealer_num) >= 17:
        #             stop 함수
        #             break
        #         elif sum(self.dealer_num) < 17:    ##### dealer의 num과 score가 필요 (str->정수화, 덱의 합 구하기)
        #             d.player.hit(b[0],b[1])




        ##### 오늘 해야할일
        # 1. Dealer의 자동 덱받기기능
        # 2. Player or Dealer가 4장 받았을 경우 일어나는 오류 처리
        # 3. Yes를 했을 때 바로 스코어가 sum으로 되는 상황 지우기
        # 4. Dealer가 A를 받았을 경우는 input을 묻지 않고 바로 계산하게끔 하는 함수
        # 5. 딜러의 num, score가 없음
        # 6.  
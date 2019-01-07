import random


class Deck:                                       ##instance 없이 쓰는 static method로 Deck.make_deck()
    deck = []

    def __init__(self):        
        print ("good")        
        if self.deck == []:
            shape = ["S","D","H","C"]
            number = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
            for i in range (0,4):
                card_shape = shape[i]
                for n in range (0, 13):
                    card_number = number[n]
                    card = card_shape + card_number
                    self.deck.append(card)
        
    # def make_deck(self):                               ## deck 을 만든다
        
    def shuffle(self):
        random.shuffle(self.deck)
       
    def pop_card(self):
        self.shuffle()
        received_card = []
        for i in range(1,3):
            card = self.deck.pop(i)
            received_card.append(card)
        return received_card

    def jqk_decision(self,deck):
        score = []
        for i in deck:
            if 'J' or 'Q' or 'K' in i[1]:
                score.append(i[1:])
            
            else :
                score.append(i[1:])
            
        # print (score)
        return score

    


class Player(Deck):
    def restart(self):
        self.deck = [] 
    def hit(self, player_deck):
                ## hit 하는거                
        player_deck.append(self.deck.pop(0))
        print("player_deck ----->", player_deck)
        print(len(self.deck))
        return player_deck
    
    def pop_card(self):
        x = super().pop_card()
        print (x)
        
    def to_int(self, score):
        num = []
        while True:
            if 'A' in score:
                a_choice = input("A는 어떤 값으로 선택하시겠습니까? 1) 1 2) 11>> ")
                if a_choice != '1' and a_choice != '2':
                    print ("Error!!! 다시입력하세요.")
                    continue
            for i in score:
                if 'J' == i or 'Q' == i or 'K' == i:        ##### line 49로 옮기는게 낫지않을까? /// Chris
                    i = 10                                      # reason why => def jqk_dec ()의 if 의미가없고 i[1:]로
                    num.append(i)                          # 다 넣어버리면 될듯
                elif 'A' == i and a_choice == "1":
                    i = 1
                    num.append(i)
                elif 'A' == i and a_choice == "2":
                    i = 11
                    num.append(i)
                else:
                    s = int(i)
                    num.append(s)
            break
        print("플레이어>>>>>>>>>", num)        
        return sum(num)


class Dealer(Deck):
    def dealer_auto_hit(self, dealer_deck):
        dealer_deck.append(self.deck.pop(0))
        print("Dealer_deck >> ", dealer_deck)
        return dealer_deck

    def to_int(self, score):
        num = []
        for i in score:

            if 'J' == i or 'Q' == i or 'K' == i:        ##### line 49로 옮기는게 낫지않을까? /// Chris
                i = 10                                      # reason why => def jqk_dec ()의 if 의미가없고 i[1:]로
                num.append(i)                          # 다 넣어버리면 될듯

            elif 'A' == i:
                continue 
            
            else: 
                s = int(i)
                num.append(s)

        if 'A' in score and sum(num) > 10:
            num.append(1)
        elif 'A' in score and sum(num) <= 10:
            num.append(11)
        print("딜러=======> " , sum(num))
        return(sum(num))

    def pop_card(self):
        x = super().pop_card()
        print(x[0])
        

while True :
    Deck.deck = []
    invite = input('게임에 참석하시겠습니까? (Yes / No)'+'\n')       ## 시작

    if invite == 'Yes' :

        player = Player()
        dealer = Dealer()

        player_received_card = player.pop_card()
        
        dealer_received_card = dealer.pop_card()
        dealer_split_num = dealer.jqk_decision(dealer_received_card)
        dealer.to_int(dealer_split_num)

        
        print("P>>>", player_received_card)
        print("D>>>", dealer_received_card)


    elif invite == 'No':
        print('>>>>>>>>>>>','다음에 만나요')
        break

    else :
        print("=============================================Error!!! 다시 입력해주세요.===============================")
        continue
       
        
    
    while True:
                                                        ## 둘째 턴 ~ 종료
        if dealer.to_int(dealer_split_num) <= 17:

            dealer_cards = dealer.dealer_auto_hit(dealer_received_card)
            dealer_split_num = dealer.jqk_decision(dealer_received_card)
            continue
        else:
            
        
            gesture = input('카드를 한장 받으시겠습니까? (Yes / No)' + '\n')

            if gesture == 'Yes':
                
                player_cards = player.hit(player_received_card)


                
                    
                player_split_num = player.jqk_decision(player_cards)
                player_result = player.to_int(player_split_num)


                
                dealer_result = dealer.to_int(dealer_split_num)
                
                # print("P>>>", dealer_cards)
                # player.score = finish.jqk_decision(player_cards)







                # finish.to_int()
                # finish.make_score()
            
            elif gesture == 'No':
                player_split_num = player.jqk_decision(player_received_card)
                player_result = player.to_int(player_split_num)
                dealer_result = dealer.to_int(dealer_split_num)
                
                if dealer_result > 21 and player_result > 21:
                    print("1>>>>>>>>>DRAW~~~ 다시 해보실???????", dealer_result, player_result)

                elif dealer_result > 21:
                    print("2>>>>>>우와 오늘 저녁은 치킨이닭!!!!!!! 한번더 이겨보실??",dealer_result, player_result)

                elif player_result > 21:
                    print("3>>>>>>>>졌어요ㅜㅜㅜㅜㅜ 이젠 기계한테도 지시네욬ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ 그냥 나갈거야?", dealer_result, player_result)
                    
                    
                elif dealer_result > player_result:
                    print("4>>>>>>>>졌어요ㅜㅜㅜㅜㅜ 이젠 기계한테도 지시네욬ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ 그냥 나갈거야?", dealer_result, player_result)
                
                elif dealer_result == player_result:
                    print("5>>>>>>>>DRAW~~~ 다시 해보실???????", dealer_result, player_result)

                else:
                    print("6>>>>>우와 오늘 저녁은 치킨이닭!!!!!!! 한번더 이겨보실??", dealer_result, player_result)

                break

            else :
                print ("Error!!!!!! 다시입력해주세요.")
                continue
    
    continue

        







        #### 오늘 해야할일
        # 1. Dealer의 자동 덱받기기능
        # 2. Player or Dealer가 4장 받았을 경우 일어나는 오류 처리
        # 3. Yes를 했을 때 바로 스코어가 sum으로 되는 상황 지우기 stop ==> sum    //// 딜러 => sum

        # 4. Dealer가 A를 받았을 경우는 input을 묻지 않고 바로 계산하게끔 하는 함수
        # 5. 딜러의 num, score가 없음
        # 6. 
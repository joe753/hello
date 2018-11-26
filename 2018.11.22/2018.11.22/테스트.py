import random


class Deck:                                       
    deck = []

    def __init__(self, name):
        self.name = name        
        print ("\n","=======>>>",self.name,"<<<=======","님이 입장하셨습니다.",)        
        if self.deck == []:
            shape = ["S","D","H","C"]
            number = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
            for i in range (0,4):
                card_shape = shape[i]
                for n in range (0, 13):
                    card_number = number[n]
                    card = card_shape + card_number
                    self.deck.append(card)
        
    def shuffle(self):
        random.shuffle(self.deck)
       
    def pop_card(self):
        self.shuffle()
        received_card = []
        for i in range(2):
            card = self.deck.pop(i)
            received_card.append(card)
        return received_card

    def collect_num(self, received_card):
        score = []
        for i in received_card:
            score.append(i[1:])
        return score

    def print_result_sum():
        print ("=====>>>", "딜러가 보유한 패의 합은 {}입니다".format(dealer_result),"<<<=====")
        print ("=====>>>", ">> User01 << 님이 보유하신 패의 합은 {}입니다".format(player_result),"<<<=====", "\n")


class Player(Deck):
    def restart(self):
        self.deck = [] 
    def hit(self, player_deck):
                ## hit 하는거                
        player_deck.append(self.deck.pop(0))
        print("\n","===== >> User01 <<님이 추가로 받으신 카드는 [ {} ]입니다. ====".format(player_deck[-1]),"\n\n","현재 패>>>>>>>", player_deck)
        return player_deck
    
    def plus_all_number(self, score):
        num = []
        while True:
            if 'A' in score:
                a_choice = input("\n" + "A는 어떤 값으로 선택하시겠습니까? 1) 1 2) 11>> ")
                if a_choice != '1' and a_choice != '2':
                    print ("Error!!! 다시입력하세요.")
                    continue
            for i in score:
                if 'J' == i or 'Q' == i or 'K' == i:       
                    i = 10                                      
                    num.append(i)                          
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
        print("\n",">> User01 <<님이 현재 보유하고 있는 카드의 합은 {} 입니다.".format(sum(num)),"\n")        
        return sum(num)


class Dealer(Deck):
    def dealer_auto_hit(self, dealer_deck):
        dealer_deck.append(self.deck.pop(0))
        return dealer_deck

    def plus_all_number(self, score):
        num = []
        for i in score:

            if 'J' == i or 'Q' == i or 'K' == i:       
                i = 10                                  
                num.append(i)                          

            elif 'A' == i:
                continue 
            
            else: 
                s = int(i)
                num.append(s)

        if 'A' in score and sum(num) > 10:
            num.append(1)
        else:
            num.append(11)
        return(sum(num))

# =============================== Main Flow =============================== #

## 시작
while True :
    Deck.deck = []
    invite = input('\n'+ '게임에 참석하시겠습니까? (Yes / No)'+'\n')       

    if invite == 'Yes' :

        player = Player("User01")
        dealer = Dealer("딜러")

        player_received_card = player.pop_card()
        
        dealer_received_card = dealer.pop_card()
        print ("\n",">> User01 <<님이 받은 카드>>>>>>>", player_received_card,"\n", "딜러가 가지고 있는 카드 >>>>>>>>>", [dealer_received_card[0]], " [**]")        
        
        dealer_only_num = dealer.collect_num(dealer_received_card)
        dealer.plus_all_number(dealer_only_num)

    elif invite == 'No':
        print('>>>>>>>>>>>','다음에 만나요')
        break

    else :
        print("=============================================Error!!! 다시 입력해주세요.===============================")
        continue

    ## 둘째 턴 ~ 종료
    while True:
                                                        
        if dealer.plus_all_number(dealer_only_num) <= 17:

            dealer_cards = dealer.dealer_auto_hit(dealer_received_card)
            dealer_only_num = dealer.collect_num(dealer_received_card)
            continue
        else:
            gesture = input("\n"+'카드를 한장 받으시겠습니까? (Yes / No)' + '\n')

            if gesture == 'Yes':
                player_cards = player.hit(player_received_card)
                player_only_num = player.collect_num(player_cards)
                player_result = player.plus_all_number(player_only_num)
                dealer_result = dealer.plus_all_number(dealer_only_num)
                
            elif gesture == 'No':
                player_only_num = player.collect_num(player_received_card)
                player_result = player.plus_all_number(player_only_num)
                dealer_result = dealer.plus_all_number(dealer_only_num)
                
                if dealer_result > 21 and player_result > 21:
                    Deck.print_result_sum()
                    print("결과┃",'\n','\t',"   ⤷ [ DRAW~~~ 다시 해보실??????? ]","\n")

                elif dealer_result > 21:
                    Deck.print_result_sum()
                    print("결과┃",'\n',"   ⤷ [ 우와 오늘 저녁은 치킨이닭!!!!!!! 한번더 이겨보실?? ]","\n")

                elif player_result > 21:
                    Deck.print_result_sum()
                    print("결과┃",'\n',"   ⤷ [ 졌어요ㅜㅜㅜㅜㅜ 이젠 기계한테도 지시네욬ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ 그냥 나갈거야? ]","\n")
                    
                elif dealer_result > player_result:
                    Deck.print_result_sum()
                    print("결과┃",'\n',"   ⤷ [ 졌어요ㅜㅜㅜㅜㅜ 이젠 기계한테도 지시네욬ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ 그냥 나갈거야? ]","\n")
                
                elif dealer_result == player_result:
                    Deck.print_result_sum()
                    print("결과┃",'\n',"   ⤷ [ DRAW~~~ 다시 해보실??????? ]","\n")

                else:
                    Deck.print_result_sum()
                    print("결과┃",'\n',"   ⤷ [ 우와 오늘 저녁은 치킨이닭!!!!!!! 한번더 이겨보실?? ]","\n")

                break

            else :
                print ("!!!!!!Error!!!!!! 다시입력해주세요. !!!!!!Error!!!!!!")
                continue
    
    continue
# -*- coding: utf-8 -*-
""" 
    BIG_ICPC
    순천향대학교 빅데이터공학과
    20171483 한태규
    
    #------------------------- memo -------------------------#
    퍼즐로 배우는 알고리즘 with Python
    
    Page num : 65
    Prac : 1
    #--------------------------------------------------------#
     
    email : gksxorb147@gmail.com
    update : 2021.04.28 22:56
"""
import random
# 인코딩 하기
def incode(hidden_card, card_info):
    
    card_info[hidden_card[0]]['trick'] = 0 # hidden : 0
    # print(card_info[hidden_card[0]])

    cardsuits = card_info[hidden_card[0]]['cardsuits']
    no_hidden = [key for key in card_info.keys() if key != hidden_card[0]]

    # Left : 1, Right : 2
    if cardsuits == 0: # C
        card_position = [1, 1, 1] # x x x hidden
        for n in range(len(no_hidden)):
            card_info[no_hidden[n]]['trick'] = card_position[n]

    elif cardsuits == 1: # D
        card_position = [2, 1, 1] # x x hidden x
        for n in range(len(no_hidden)):
            card_info[no_hidden[n]]['trick'] = card_position[n]

    elif cardsuits == 2: # H
        card_position = [2, 2, 1] # x hidden x x 
        for n in range(len(no_hidden)):
            card_info[no_hidden[n]]['trick'] = card_position[n]

    elif cardsuits == 3: # S
        card_position = [2, 2, 2] # hidden x x x
        for n in range(len(no_hidden)):
            card_info[no_hidden[n]]['trick'] = card_position[n]

    # 가로 세로, 앞, 뒤
    cnumbers = card_info[hidden_card[0]]['cnumbers']
    # card_state1 : 앞 : 0, 뒤 : 1
    # card_state2 : 세로 : 0, 가로 : 1
    if cnumbers == 1:
        card_state1 = [0, 0, 0] # 앞, 앞, 앞
        card_state2 = [0, 0, 0] # 세로, 세로, 세로
        for n in range(len(no_hidden)):
            card_info[no_hidden[n]]['state1'] = card_state1[n]
            card_info[no_hidden[n]]['state2'] = card_state2[n]

    elif cnumbers == 2:
        card_state1 = [1, 0, 0] # 앞, 앞, 앞
        card_state2 = [0, 0, 0] # 세로, 세로, 세로
        for n in range(len(no_hidden)):
            card_info[no_hidden[n]]['state1'] = card_state1[n]
            card_info[no_hidden[n]]['state2'] = card_state2[n]

    elif cnumbers == 3:
        card_state1 = [0, 1, 0] # 앞, 앞, 앞
        card_state2 = [0, 0, 0] # 세로, 세로, 세로
        for n in range(len(no_hidden)):
            card_info[no_hidden[n]]['state1'] = card_state1[n]
            card_info[no_hidden[n]]['state2'] = card_state2[n]

    elif cnumbers == 4:
        card_state1 = [0, 0, 1] # 앞, 앞, 앞
        card_state2 = [0, 0, 0] # 세로, 세로, 세로
        for n in range(len(no_hidden)):
            card_info[no_hidden[n]]['state1'] = card_state1[n]
            card_info[no_hidden[n]]['state2'] = card_state2[n]

    elif cnumbers == 5:
        card_state1 = [1, 1, 0] # 앞, 앞, 앞
        card_state2 = [0, 0, 0] # 세로, 세로, 세로
        for n in range(len(no_hidden)):
            card_info[no_hidden[n]]['state1'] = card_state1[n]
            card_info[no_hidden[n]]['state2'] = card_state2[n]
        
    elif cnumbers == 6:
        card_state1 = [1, 0, 1] # 앞, 앞, 앞
        card_state2 = [0, 0, 0] # 세로, 세로, 세로
        for n in range(len(no_hidden)):
            card_info[no_hidden[n]]['state1'] = card_state1[n]
            card_info[no_hidden[n]]['state2'] = card_state2[n]

    elif cnumbers == 7:
        card_state1 = [0, 1, 1] # 앞, 앞, 앞
        card_state2 = [0, 0, 0] # 세로, 세로, 세로
        for n in range(len(no_hidden)):
            card_info[no_hidden[n]]['state1'] = card_state1[n]
            card_info[no_hidden[n]]['state2'] = card_state2[n]

    elif cnumbers == 8:
        card_state1 = [1, 1, 1] # 앞, 앞, 앞
        card_state2 = [0, 0, 0] # 세로, 세로, 세로
        for n in range(len(no_hidden)):
            card_info[no_hidden[n]]['state1'] = card_state1[n]
            card_info[no_hidden[n]]['state2'] = card_state2[n]

    elif cnumbers == 9:
        card_state1 = [0, 0, 0] # 앞, 앞, 앞
        card_state2 = [1, 0, 0] # 세로, 세로, 세로
        for n in range(len(no_hidden)):
            card_info[no_hidden[n]]['state1'] = card_state1[n]
            card_info[no_hidden[n]]['state2'] = card_state2[n]

    elif cnumbers == 10:
        card_state1 = [0, 0, 0] # 앞, 앞, 앞
        card_state2 = [0, 1, 0] # 세로, 세로, 세로
        for n in range(len(no_hidden)):
            card_info[no_hidden[n]]['state1'] = card_state1[n]
            card_info[no_hidden[n]]['state2'] = card_state2[n]

    elif cnumbers == 11:
        card_state1 = [0, 0, 0] # 앞, 앞, 앞
        card_state2 = [0, 0, 1] # 세로, 세로, 세로
        for n in range(len(no_hidden)):
            card_info[no_hidden[n]]['state1'] = card_state1[n]
            card_info[no_hidden[n]]['state2'] = card_state2[n]

    elif cnumbers == 12:
        card_state1 = [0, 0, 0] # 앞, 앞, 앞
        card_state2 = [1, 1, 0] # 세로, 세로, 세로
        for n in range(len(no_hidden)):
            card_info[no_hidden[n]]['state1'] = card_state1[n]
            card_info[no_hidden[n]]['state2'] = card_state2[n]

    elif cnumbers == 13:
        card_state1 = [0, 0, 0] # 앞, 앞, 앞
        card_state2 = [1, 0, 1] # 세로, 세로, 세로
        for n in range(len(no_hidden)):
            card_info[no_hidden[n]]['state1'] = card_state1[n]
            card_info[no_hidden[n]]['state2'] = card_state2[n]

    elif cnumbers == 13:
        card_state1 = [0, 0, 0] # 앞, 앞, 앞
        card_state2 = [0, 1, 1] # 세로, 세로, 세로
        for n in range(len(no_hidden)):
            card_info[no_hidden[n]]['state1'] = card_state1[n]
            card_info[no_hidden[n]]['state2'] = card_state2[n]

    return card_info

def ComputerAssistant():
  
    # print ('Cards are character strings as shown below.')
    # print ('Ordering is:', deck)
    cards, cind, cardsuits, cnumbers = [], [], [], []
    numsuits = [0, 0, 0, 0]
    card_info = {}

    # 랜덤으로 4장 추출
    choice_list = random.sample(deck, 4)
    print('choice_list :', choice_list)

    # 뽑은 4장의 카드 dict화
    for i in range(len(choice_list)):

        card_name = choice_list[i]

        # 뽑은 카드의 정보 입력
        card_info[card_name] = {}
        card_info[card_name]['deck_index_num'] = deck.index(card_name)

        card_info[card_name]['cardsuits'] = card_info[card_name]['deck_index_num'] // 13 #  이부분 변경
        card_info[card_name]['cnumbers'] = card_info[card_name]['deck_index_num'] % 13 + 1
        
        index_num = card_info[card_name]['deck_index_num']

    # print('card_info :', card_info)

    # hidden 카드 뽑기
    hidden_card = random.sample(choice_list, 1)
    print('hidden_card :', hidden_card[0])

    # 인코딩 하기
    card_info = incode(hidden_card, card_info)

    for key, value in card_info.items():
        print(key, value)

    # 카드 표현하기
    for key, value in card_info.items():
        if value['trick'] == 1:
            print(key, '왼쪽', '> 앞,뒤 :', value['state1'],  '> 가로,세로 :', value['state2'])
        elif value['trick'] == 0:
            print('숨겨진 카드 : ???', key)
        elif value['trick'] == 2:
            print(key, '오른쪽',  '> 앞,뒤 :', value['state1'],  '> 가로,세로 :', value['state2'])

    guess = input('What is the hidden card? : ')
    if guess == hidden_card[0]:
        print ('You are a Mind Reader Extraordinaire!')
    else:
        print ('Sorry, not impressed!')

    return

# -------------------- 인코딩 함수 만들기 -------------------- #

if __name__=="__main__":

  deck = [ 'A_C', '2_C', '3_C', '4_C', '5_C', '6_C', '7_C', '8_C', '9_C', '10_C', 'J_C', 'Q_C', 'K_C', 
           'A_D', '2_D', '3_D', '4_D', '5_D', '6_D', '7_D', '8_D', '9_D', '10_D', 'J_D', 'Q_D', 'K_D',
           'A_H', '2_H', '3_H', '4_H', '5_H', '6_H', '7_H', '8_H', '9_H', '10_H', 'J_H', 'Q_H', 'K_H',
           'A_S', '2_S', '3_S', '4_S', '5_S', '6_S', '7_S', '8_S', '9_S', '10_S', 'J_S', 'Q_S', 'K_S' ]

  # input_card = ['Q_H', '10_D', '8_H', '9_S']

  ComputerAssistant()
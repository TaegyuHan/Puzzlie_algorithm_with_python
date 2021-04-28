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
    update : 2021.04.27 21:36
"""

import random

def outputFirstCard(numbers, oneTwo, cards):

    encode = (numbers[oneTwo[0]] - numbers[oneTwo[1]]) % 13
    if encode > 0 and encode <= 6:
        hidden = oneTwo[0]
        other = oneTwo[1]
    else:
        hidden = oneTwo[1]
        other = oneTwo[0]
        encode = (numbers[oneTwo[1]] - numbers[oneTwo[0]]) % 13

##    #The following print statement is just for debugging!
##    print ('Hidden card is:', cards[hidden], 'and need to encode', encode)
    print ('First card is:', cards[other])

    return hidden, other, encode

def sortList(tlist):
    for index in range(0, len(tlist)-1):
        ismall = index
        for i in range(index, len(tlist)):
            if tlist[ismall] > tlist[i]:
                ismall = i
        tlist[index], tlist[ismall] = tlist[ismall], tlist[index]
    
    return

def outputNext3Cards(code, ind):
    
    if code == 1:
        second, third, fourth = ind[0], ind[1], ind[2]
    elif code == 2:
        second, third, fourth = ind[0], ind[2], ind[1]
    elif code == 3:
        second, third, fourth = ind[1], ind[0], ind[2]       
    elif code == 4:
        second, third, fourth = ind[1], ind[2], ind[0]
    elif code == 5:
        second, third, fourth = ind[2], ind[0], ind[1]
    else:
        second, third, fourth = ind[2], ind[1], ind[0]

    print ('Second card is:', deck[second])
    print ('Third card is:', deck[third])
    print ('Fourth card is:', deck[fourth])

def ComputerAssistant(input_list):
  
    print ('Cards are character strings as shown below.')
    print ('Ordering is:', deck)
    cards, cind, cardsuits, cnumbers = [], [], [], []
    numsuits = [0, 0, 0, 0]
    card_info = {}

    # 랜덤으로 5장 추출
    # choice_list = random.sample(deck, 5)
    choice_list = input_list
    print(choice_list)

    for i in range(5):
        # number = number * (i + 1) // (i + 2)
        # n = number % 5

        card_name = choice_list[i]

        # 뽑은 카드의 정보 입력
        card_info[card_name] = {}
        card_info[card_name]['deck_index_num'] = deck.index(card_name)

        card_info[card_name]['cardsuits'] = card_info[card_name]['deck_index_num'] % 4
        card_info[card_name]['cnumbers'] = card_info[card_name]['deck_index_num'] // 4
        
        index_num = card_info[card_name]['deck_index_num']

        # numsuits[index_num % 4] += 1
        # if numsuits[index_num % 4] > 1:s
        #     pairsuit = index_num % 4

    print(card_info)

    # 만약 같은 기호를 가진 카드들이 두 그룹이 있는 경우에는
    # 비밀 카드와 첫 번째 카드 사이에 거리가 더욱 짧은 카드 
    # 그룹을 선택 하도록 해주세요

    two_more_card = {} # 두개 이상 카드 dict 생성
    for suits in range(5):
        cnumber_list = []
        for v in card_info.values():
            if v['cardsuits'] == suits:
                cnumber_list.append(v['cnumbers'])
                
        if len(cnumber_list) > 1:
            two_more_card[suits] = cnumber_list

    print('two_more_card :', two_more_card)

    # 더욱 짧은 범위 찾기
    # 차이가 적은것 저장
    
    min_dif = 0
    for suits, v in two_more_card.items():
        difference = 0
        for n in range(len(v)):

            if n == 0:
                before_dif = v[n]
                print(before_dif)
                continue
            
            difference1 = abs(before_dif - v[n])

            if before_dif < v[n]:
                difference2 = (before_dif - 1) + (14 - v[n])
            else: pass

            print('difference1 : ', difference1)
            print('difference2 : ', difference2)
                
            if min_dif == 0:
                if difference1 > difference2:
                    min_dif = difference2
                    pairsuit = suits
                else:
                    min_dif = difference1
                    pairsuit = suits
                continue

            if min_dif > difference1:
                pairsuit = suits
            elif min_dif > difference2:
                pairsuit = suits

        print("min_dif :", min_dif)

    print('pairsuit :', pairsuit)

    cardh = []
    i = 0
    for key, value in card_info.items():
        if value['cardsuits'] == pairsuit:
            cardh.append(i)
        i += 1

    print('cardh : ', cardh)

    # # cardh = []
    # # for i in range(5):
    # #     if cardsuits[i] == pairsuit:
    # #         cardh.append(i)
    # # print('cardh : ', cardh)    

    cnumbers = [v['cnumbers'] for v in card_info.values()]
    cards = [k for k in card_info]

    hidden, other, encode = outputFirstCard(cnumbers, cardh, cards)

    remindices = []
    for v in card_info.values():
        if i != hidden and i != other:
            remindices.append(v['deck_index_num'])

    # # for i in range(5):
    # #     if i != hidden and i != other:
    # #         remindices.append(cind[i])

    sortList(remindices)
    outputNext3Cards(encode, remindices)

    print('cards :', cards)
    print('hidden :', hidden)


    guess = input('What is the hidden card? : ')
    if guess == cards[hidden]:
        print ('You are a Mind Reader Extraordinaire!')
    else:
        print ('Sorry, not impressed!')

    return


if __name__=="__main__":

  deck = [  'A_C', 'A_D', 'A_H', 'A_S'
          , '2_C', '2_D', '2_H', '2_S'
          , '3_C', '3_D', '3_H', '3_S'
          , '4_C', '4_D', '4_H', '4_S'
          , '5_C', '5_D', '5_H', '5_S'
          , '6_C', '6_D', '6_H', '6_S'
          , '7_C', '7_D', '7_H', '7_S'
          , '8_C', '8_D', '8_H', '8_S'
          , '9_C', '9_D', '9_H', '9_S'
          , '10_C', '10_D', '10_H', '10_S'
          , 'J_C', 'J_D', 'J_H', 'J_S'
          , 'Q_C', 'Q_D', 'Q_H', 'Q_S'
          , 'K_C', 'K_D', 'K_H', 'K_S' ]

  input_list = ['3_H', '8_H', 'J_C', 'K_C', '9_D']

  ComputerAssistant(input_list)

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
        second, third,
         fourth = ind[2], ind[0], ind[1]
    else:
        second, third, fourth = ind[2], ind[1], ind[0]

    print ('Second card is:', deck[second])
    print ('Third card is:', deck[third])
    print ('Fourth card is:', deck[fourth])

def ComputerAssistant():
  
    print ('Cards are character strings as shown below.')
    print ('Ordering is:', deck)
    cards, cind, cardsuits, cnumbers = [], [], [], []
    numsuits = [0, 0, 0, 0]
    #number = int(input("Please give random number of" + 'at least 6 digits:'))

    # 랜덤으로 5장 추출
    choice_list = [random.choice(deck) for i in range(5)]
    print(choice_list)

    for i in range(5):
        # number = number * (i + 1) // (i + 2)
        # n = number % 5

        # 뽑은 카드의 정보 입력
        cd_info = choice_list[i]
        index_num = deck.index(cd_info)

        cards.append(cd_info)
        cind.append(index_num)
        cardsuits.append(index_num % 4)
        cnumbers.append(index_num // 4)
        numsuits[index_num % 4] += 1
        if numsuits[index_num % 4] > 1:
            pairsuit = index_num % 4
    
##    #Just for debugging
##    print (cards)
    cardh = []
    for i in range(5):
        if cardsuits[i] == pairsuit:
            cardh.append(i)

    hidden, other, encode = outputFirstCard(cnumbers, cardh, cards)

    remindices = []
    for i in range(5):
        if i != hidden and i != other:
            remindices.append(cind[i])

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

  ComputerAssistant()
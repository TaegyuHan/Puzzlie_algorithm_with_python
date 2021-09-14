# 메모리 사용량 최적화 하기
import itertools

def check_list(guestList, dislikePairs):
    """ 싫어 하는 사람이 있는 사람과
        없는 사람을 나누는 함수

    Args:
        guestList ([list]]): [손님 리스트]
        dislikePairs ([list]): [싫어하는 쌍]

    Returns:
        [list]: [싫어하는 사람이 있는사람 / 없는 사람]
    """
    # 싫어하는 사람이 있는 사람 집합으로 만들기

    # print(guestList, dislikePairs)

    dislike_people = set(itertools.chain(*dislikePairs))

    have_dislike = [] # 싫어 하는 사람이 있는 사람
    like = [] # 싫어 하는 사람이 없느 사람

    for man in guestList:
        if man[0] in dislike_people:
            have_dislike.append(man)
        else:
            like.append(man)

    # print(like, have_dislike)

    return like, have_dislike


def check_like_high(guestList, dislikePairs):

    # print(guestList, dislikePairs)
    max_pairs = [] # 애정도가 가장 높은 1쌍
    max_like_sum = 0 # 애정도 저장 값

    # 딕셔너리로 변환
    guestListDict = dict(guestList)

    for pairs in dislikePairs:
        tmp_like_sum = 0
        for man in pairs: # 딕셔너리 안에서 값 꺼냄
            tmp_like_sum += guestListDict[man]

        #  가장 큰 값 생성
        if tmp_like_sum > max_like_sum:
            max_like_sum = tmp_like_sum
            max_pairs = pairs

    # 1쌍 찾기
    pair1 = (max_pairs[0], guestListDict[max_pairs[0]])
    pair2 = (max_pairs[1], guestListDict[max_pairs[1]])

    # 1쌍 제거
    del guestList[guestList.index(pair1)]
    del guestList[guestList.index(pair2)]

    # 1쌍에 연결되어 제거되는 사람 찾기
    order_max = [pair1, pair2]
    delete_set = set() # 제거 될 사람 저장 공간
    for pairs in dislikePairs:
        for str in order_max:
            if str[0] in pairs:
                delete_set.update(pairs)

    # guestList 에서 제거하기
    # 1쌍에 연결 안된 사람 추출
    guestList = [man for man in guestList if man[0] not in delete_set]
    # print(guestList)
    print(dislikePairs) # dislikePairs 제거 해야함 

    return guestList, order_max


def choose_another_friend(guestList, dislikePairs):

    # 가장 큰 값 찾기
    max_index = 0
    for man in guestList:
        if max_index < man[1]:
            max_index = guestList.index(man)

    # 가장 큰값 꺼내기
    max_friend = guestList.pop(max_index-1)
    # print(max_friend)

    # print(guestList, dislikePairs)


def IniteDinnerOptimized(guestList, dislikePairs):

    # 싫어하는 사람이 없는 사람 제외
    exception_people, guestList = \
        check_list(guestList, dislikePairs)

    # 친밀 도가 가장 높은
    # 서로 싫어하는 1쌍 추출
    # 및 다른 연결 쌍 제거
    guestList, max_pairs = \
        check_like_high(guestList, dislikePairs)

    # print(guestList, dislikePairs, max_pairs)

    # 친밀도가 가장 높은 1쌍과 연결된 다른 사람 제거
    choose_another_friend(guestList, dislikePairs)

    # print(exception_people, guestList)
    n, invite = len(guestList), []
    invite += max_pairs
    invite += exception_people
    # for i in range(2**n):
    #     Combination = []
    #     num = i
    #     for j in range(n):
    #         if (num % 2 == 1):
    #             Combination = [guestList[n-1-j]] + Combination
    #         num = num // 2
    #     good = True
    #
    #     for j in dislikePairs:
    #         if j[0] in Combination and j[1] in Combination:
    #             good = False
    #
    #     if good:
    #         if len(Combination) > len(invite):
    #             invite = Combination


    # 제외 했던 사람 추가
    print("Optimun Solution: ", invite)


if __name__ == '__main__':
    LargeDislikes = [['B','C'],['C','D'],['D','E'],['F','G'],
                     ['F','H'],['F','I'],['G','H']]

    LargeGustList = [('A',2),('B',1),('C',3),
                     ('D',2),('E',1),('F',4),
                     ('G',2),('H',1),('I',3)]
                     
    IniteDinnerOptimized(LargeGustList, LargeDislikes)
    # 정답 : Optimun Solution:  ['Alice', 'Eve', 'Cleo', 'Don']




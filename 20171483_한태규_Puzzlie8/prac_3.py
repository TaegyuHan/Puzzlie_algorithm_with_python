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

    return max_pairs


def pair_del(max_pairs, dislikePairs):

    print(dislikePairs)

    i = 0
    for pairs in dislikePairs:
        for man in max_pairs:
            if(man == pairs[0] or man == pairs[1]):
                print(man)
                print(pairs)
                del dislikePairs[dislikePairs.index(pairs)]
                break

    print(dislikePairs)

def IniteDinnerOptimized(guestList, dislikePairs):

    # 싫어하는 사람이 없는 사람 제외
    exception_people, guestList = \
        check_list(guestList, dislikePairs)

    # 친밀 도가 가장 높은
    # 서로 싫어하는 1쌍 추출
    # 및 다른 연결 쌍 제거
    max_pairs = check_like_high(guestList, dislikePairs)
    # print(max_pairs)

    # 친밀도 가장 높은 1쌍 과 연결된
    # 쌍 제거
    # ######< 이부분 해결해야 한다.
    pair_del(max_pairs, dislikePairs)


    # print(exception_people, guestList)
    n, invite = len(guestList), []

    for i in range(2**n):
        Combination = []
        num = i
        for j in range(n):
            if (num % 2 == 1):
                Combination = [guestList[n-1-j]] + Combination
            num = num // 2
        good = True

        for j in dislikePairs:
            if j[0] in Combination and j[1] in Combination:
                good = False

        if good:
            if len(Combination) > len(invite):
                invite = Combination


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



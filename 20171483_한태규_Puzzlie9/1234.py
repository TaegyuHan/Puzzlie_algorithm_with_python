Talents = ["Sing", "Dance", "Magic", "Act", "Flex", "Code"]
Candidates = ["Aly", "Bob", "Cal", "Don", "Eve", "Fay"]
CandidateTalents = [["Flex", "Code"], ["Dance", "Magic"], 
                    ["Sing", "Magic"], ["Sing", "Dance"], 
                    ["Dance", "Act", "Code"], ["Act", "Code"]]


def Good(Comb: list, candList: list, candTalents: list, AllTalents: list):
    """선택된 참가자의 프로그램에 모든 재능이
       방송 되는지 확인한다.

    Args:
        Comb (list): [선택 참가자]
        candList (list): [모든 참가자]
        candTalents (list): [참가자 각각의 재능]
        AllTalents (list): [참가자의 모든 재능]

    Returns:
        [bool]: [모든 재능을 포함했는지 확인합니다.]
    """

    for tal in AllTalents:  # 모든 재능 검사
        cover = False
        for cand in Comb:  # 선택 참가자 1명씩 검사
            candTal = candTalents[candList.index(cand)]
            if tal in candTal:  # 있으면 통과
                cover = True
        if not cover:  # 없으면  False
            return False

    return True  # 있으면  True


def Hire4Show(candList: list, candTalents: list, talentList: list):
    """최소한의 후보를 출력합니다.

    Args:
        candList (list): [모든 참가자]
        candTalents (list): [모든 참가자의 재능]
        talentList (list): [재능]
    """

    # prac 1
    # 제거 하는 함수 생성
    # candList, candTalents = check_overlap_talent(candList, candTalents)

    n = len(candList)
    print(n)
    hire = candList[:]
    
    # print(candList)

    # 모든 경우의 수
    for i in range(2**n):
        Combination = []
        num = i
        print(f"num : {num}")

        # 조합 뽑기
        for j in range(n):
            if (num % 2 == 1):
                print(f"{num} % 2 == 1 : {num % 2 == 1}")
                Combination = [candList[n-1-j]] + Combination
            num = num // 2
            
        # 모든 재능 만족하는지 확인
        if Good(Combination, candList, candTalents, talentList):
            if len(hire) > len(Combination):
              hire = Combination
        # print(Combination)

    print("Optimum Solution: ", hire)


Hire4Show(Candidates, CandidateTalents, Talents)
def Good(Comb: list, candList: list, candTalents: list, AllTalents: list):
    """선택된 참가자의 프로그램에 모든 재능이
       방송 되는지 확인한다.

    Args:
        Comb (set): [선택 참가자]
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


def chcek_candidates(chosen, elts):
    global Talents, Candidates, \
        CandidateTalents, result

    if not elts:
        if Good(chosen, Candidates, CandidateTalents, Talents):
            if len(result) > len(chosen):
                result = chosen
        return

    for i, elt in enumerate(elts):
            chcek_candidates(chosen + [elt], elts[:i] + elts[i+1:])
            chcek_candidates(chosen, elts[:i] + elts[i + 1:])


if __name__ == '__main__':
    Talents = ["Sing", "Dance", "Magic", "Act", "Flex", "Code"]
    Candidates = ["Aly", "Bob", "Cal", "Don", "Eve", "Fay"]
    CandidateTalents = [["Flex", "Code"], ["Dance", "Magic"],
                        ["Sing", "Magic"], ["Sing", "Dance"],
                        ["Dance", "Act", "Code"], ["Act", "Code"]]
    result = Candidates
    chcek_candidates([], Candidates)
    print(result)
    #  ['Aly', 'Cal', 'Eve']

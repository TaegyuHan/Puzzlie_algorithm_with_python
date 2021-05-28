""" 
    BIG_ICPC
    순천향대학교 빅데이터공학과
    20171483 한태규
    
    #------------------------- memo -------------------------#
    퍼즐로 배우는 알고리즘 with Python
    
    Page num : 34
    Prac : 1
    #--------------------------------------------------------#
     
    email : gksxorb147@gmail.com
    update : 2021.03.29 00:11
"""

def pleaseConform(caps):
    
    #Initialization
    start = 0
    forward = 0
    backward = 0
    intervals = []

    # 손님의 패턴을 찾아 
    # 리스트로 만드는 for 문
    for i in range(len(caps)):
        if caps[start] != caps[i]:
            # each interval is a tuple with 3 elements (start, end, type)
            intervals.append((start, i - 1, caps[start]))
            if caps[start] == 'F':
                forward += 1
            else:
                backward += 1
            start = i
    
    #Need to add the last interval after for loop completes execution
    intervals.append((start, len(caps) - 1, caps[start]))
    # [(0, 1, 'F'), (2, 4, 'B'), (5, 5, 'F'), (6, 6, 'B'), (7, 12, 'F')]

    if caps[start] == 'F':
        forward += 1
    else:
        backward += 1

    if forward < backward:
        flip = 'F'
    else:
        flip = 'B'

    for t in intervals:
        if t[2] == flip:
            #Exercise: if t[0] == t[1] change the printing!
            if t[0] == t[1]: 
                ## 마지막 자연스럽게 나오게 코드 수정
                if intervals[-1] == t or intervals[-2] == t: ## 코드 추가
                    print ('People at positions', t[0], 'flip your cap!') ## 코드 추가
                    break
            else:
                print ('People in positions', t[0], 'through', t[1], 'flip your caps!')





if __name__=="__main__":

    caps = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'F', 'F', 'F', 'F', 'F', 'F' ]

    pleaseConform(caps)
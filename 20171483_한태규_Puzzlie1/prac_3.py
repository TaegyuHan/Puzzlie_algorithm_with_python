""" 
    BIG_ICPC
    순천향대학교 빅데이터공학과
    20171483 한태규
    
    #------------------------- memo -------------------------#
    퍼즐로 배우는 알고리즘 with Python
    
    Page num : 35
    Prac : 3
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
    
    if caps.count('F') < caps.count('B'):
        flip = 'F'
    else:
        flip = 'B'

    for t in intervals:
        if t[2] == flip:
            #Exercise: if t[0] == t[1] change the printing!
            if t[0] == t[1]:
                print ('People in positions', t[0], 'flip your cap!') ## 코드 추가
            else:
                print ('People in positions', t[0], 'through', t[1], 'flip your caps!')
    
    print(intervals)

if __name__=="__main__":

    caps = ['H','F', 'F', 'B', 'H', 'B', 'F', 'B', 'B','H', 'B', 'F', 'H', 'H', 'F', 'F']

    pleaseConform(caps)

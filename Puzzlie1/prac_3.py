
caps = ['F', 'F', 'B', 'H', 'B', 'F', 'B', 'B', 'B', 'F', 'H', 'F', 'F']

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
                if intervals[-1] == t or intervals[-2] == t: ## 코드 추가
                    print ('People at positions', t[0], 'flip your cap!') ## 코드 추가
                else:
                    print ('People in positions', t[0], 'flip your cap!') ## 코드 추가
            else:
                print ('People in positions', t[0], 'through', t[1], 'flip your caps!')

if __name__=="__main__":

    pleaseConform(caps)

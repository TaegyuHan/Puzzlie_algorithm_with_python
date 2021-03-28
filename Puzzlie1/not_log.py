# Programming for the Puzzled -- Srini Devadas
# You Will All Conform
# Input is a vector of F's and B's, in terms of forwards and backwards caps
# Output is a set of commands (printed out) to get either all F's or all B's
# Fewest commands are the goal

#caps = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'F', 'F', 'F', 'F', 'F', 'F' ]
#caps = ['F', 'B', 'F']

cap2 = ['B', 'F', 'B', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'F', 'B']

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
    
    if caps[start] == 'F':
        forward += 1
    else:
        backward += 1

    if forward < backward:
        flip = 'F'
    else:
        flip = 'B'

    # print(flip)
    for t in intervals:
        if t[2] == flip:
            #Exercise: if t[0] == t[1] change the printing!
            if t[0] == t[1]:
                if intervals[-1] == t or intervals[-2] == t:
                    print ('People at positions', t[0], 'flip your cap!') 
                else:
                  print ('People in positions', t[0], 'flip your cap!')
            else:
                print ('People in positions', t[0], 'through', t[1], 'flip your caps!')

        


def pleaseConformOnepass(caps):
    try:
        caps = caps + [caps[0]]
        for i in range(1, len(caps)):
            if caps[i] != caps[i-1]:
                if caps[i] != caps[0]:
                    print('People in positions', i, end='')
                else:
                    print(' through', i-1, 'flip your caps!')
    except IndexError as e:
        print("Error :",e)
        print("리스트가 비어있어 인덱싱에 실패했습니다.")
        


pleaseConform(cap2)
#pleaseConformOnepass(caps)


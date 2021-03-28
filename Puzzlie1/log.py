# Programming for the Puzzled -- Srini Devadas
# You Will All Conform
# Input is a vector of F's and B's, in terms of forwards and backwards caps
# Output is a set of commands (printed out) to get either all F's or all B's
# Fewest commands are the goal


caps = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F' ]
#caps = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'F', 'F', 'F', 'F', 'F', 'F' ]
#cap2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F' ]
#caps = ['F', 'B', 'F']

result = []

def pleaseConform(caps):
    
    print("#-------------------- pleaseConform start --------------------#")
    
    print("caps :", caps)
    
    #Initialization
    start = 0; print("start :", start)
    forward = 0; print("forward :", forward)
    backward = 0; print("backward :", backward)
    intervals = []; print("intervals :", intervals)


    
    print("#-------------------- for start --------------------#")

    for i in range(len(caps)):
        print("for > i : {}".format(i))
        print("if caps[start] != caps[i]: > " + caps[start] + ' != ' + caps[i])
        if caps[start] != caps[i]:
            print("#---------- 1 > if start ----------#")
            # each interval is a tuple with 3 elements (start, end, type)
            print('start :', start, end=" | ")
            print('i :', i, end=" | ")
            print('caps[start] :', caps[start])
            print("intervals.append > ", end=' ')
            print((start, i - 1, caps[start]))
            intervals.append((start, i - 1, caps[start]))
            print("intervals :", intervals)
            
            print("if caps[start] == 'F' > " + caps[start] + " == F")
            if caps[start] == 'F':
                print("#---------- 2 > if start ----------#")
                forward += 1
                print('forward : {}'.format(forward))
                print("#---------- 2 > if end ----------#")
            else:
                print("#---------- 2 > if start ----------#")
                backward += 1
                print('backward : {}'.format(backward))
                print("#---------- 2 > if end ----------#")
            start = i
            print('start =', i)
            print("#---------- 1 > if end ----------#")

    print("#--------------------  for end  --------------------#")
    
#Need to add the last interval after for loop completes execution
    intervals.append((start, len(caps) - 1, caps[start]))
    print("intervals.append > ", end=' ')
    print((start, i - 1, caps[start]))
                    #  [0 ,11, 'F']
    
    print("if caps[start] == 'F' > " + caps[start] + " == F")
    if caps[start] == 'F':
        print("#---------- 1 > if start ----------#")
        forward += 1
        print('forward : {}'.format(forward))
        print("#---------- 1 > if end ----------#")
    else:
        print("#---------- 1 > if start ----------#")
        backward += 1
        print('backward : {}'.format(backward))
        print("#---------- 1 > if end ----------#")
 
    
    print("if forward < backward > " + str(forward) + " < " + str(backward))
    if forward < backward:
        print("#---------- 1 > if start ----------#")
        flip = 'F'
        print('flip :', flip)
        print("#---------- 1 > if end ----------#")
    else:
        print("#---------- 1 > if start ----------#")
        flip = 'B'
        print('flip :', flip)
        print("#---------- 1 > if end ----------#")
        
        
    print("#-------------------- for start --------------------#")        
        
    print("intervals :", intervals)
    for t in intervals:
        print("t :",t, end=" > ")
         
        print("if t[2] == flip >", t[2], "==", flip)
        if t[2] == flip:
            print("#---------- 1 > if start ----------#")
            #Exercise: if t[0] == t[1] change the printing!
            print("if t[0] == t[1] > ", t[0], "==", t[1])
            if t[0] == t[1]:
                print("#---------- 2 > if start ----------#")
                print ('Person at position', t[0], 'flip your cap!')
                print("#---------- 2 > if end ----------#")
            else:
                print("#---------- 2 > if start ----------#")
                print ('People in positions', t[0], 'through', t[1], 'flip your caps!')
                print("#---------- 2 > if end ----------#")
            print("#---------- 1 > if end ----------#")
    print("#--------------------  for end  --------------------#")
                
    
    print("#-------------------- pleaseConform end --------------------#")
            
#pleaseConform(caps)



def pleaseConformOnepass(caps):
    try:
        print("capas :", caps)
        caps = caps + [caps[0]]
        print("caps = caps + [caps[0]] :", caps)

        print("#-------------------- for start --------------------#")

        for i in range(1, len(caps)):
            print("for > i :", i)
            
            print("if caps[i] != caps[i-1]: > ", caps[i], "!=", caps[i-1])
            if caps[i] != caps[i-1]:
                print("#---------- 1 > if start ----------#")
                print("if caps[i] != caps[0]: > ", caps[i], "!=", caps[0])
                if caps[i] != caps[0]:
                    print("#---------- 2 > if start ----------#")
                    print('People in positions', i)
                    print("#---------- 1 > if end ----------#")
                else:
                    print("#---------- 2 > if start ----------#")
                    print(' through', i-1, 'flip your caps!')
                    print("#---------- 2 > if end ----------#")
                print("#---------- 1 > if end ----------#")
        print("#--------------------  for end  --------------------#")

    except IndexError as e:
        print("Error :",e)
        print("리스트가 비어있어 인덱싱에 실패했습니다.")


# pleaseConformOnepass(caps)
pleaseConform(caps)
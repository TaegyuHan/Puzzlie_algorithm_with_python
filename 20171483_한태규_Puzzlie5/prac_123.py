def howHardIsTheCrystal(n, d):

    # 밑 찾기
    
    # 층  n : 128
    # 구슬 개수 d : 8

    r = 1
    while (r**d <= n):
        r = r + 1
        
    # if r**d > n:
    #     r -= 1

    print('r :', r)
    
    # prac_1 추가
    # 사용하는 구슬 개수 찾기
    for i in range(d):
        if r**i >= n:
            beads_use_cnt = i
            break
        else: continue
    print('beads_use_cnt :', beads_use_cnt)

    numDrops = 0
    floorNoBreak = [0] * beads_use_cnt
    
    # prac_3 추가
    start_section = 0
    end_section = n

    ## prac_2 추가
    beads_break = 0
    print('floorNoBreak :', floorNoBreak)
    
    for i in range(beads_use_cnt):
        
        for j in range(r - 1):
            floorNoBreak[i] += 1
            print('for > floorNoBreak', floorNoBreak)
            Floor = convertToDecimal(r, beads_use_cnt, floorNoBreak)
            print(Floor)

            if Floor > n:
                floorNoBreak[i] -= 1
                break

            print ('Drop ball', i+1, 'from Floor', Floor)
            print("Check Section [{}:{}]".format(start_section, end_section))
            yes = input('Did the ball break (yes/no)?:')
            numDrops += 1
            if yes == 'yes':
                floorNoBreak[i] -= 1
                ## prac_2 추가
                beads_break += 1
                print("현재 부숴진 구슬 개수 :", beads_break)

                # prac_3 추가
                end_section = Floor
                break
            ## prac_2 추가
            else:
                start_section = Floor
                print("현재 부숴진 구슬 개수 :", beads_break)

    hardness = convertToDecimal(r, beads_use_cnt, floorNoBreak)
    print("Check Section [{}:{}]".format(start_section, end_section))
    print('Hardness coefficient is', hardness)
    print('Total number of drops is', numDrops)

    return

def convertToDecimal(r, d, rep):
    number = 0
    for i in range(d-1):
        
        number = (number + rep[i]) * r
    number += rep[d-1]
    print(number)
    return number


if __name__ == '__main__':
    howHardIsTheCrystal(128, 6)
    
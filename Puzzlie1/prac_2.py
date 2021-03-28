
cap2 = ['F','B','F','B', 'F','F', 'B', 'F', 'B', 'B', 'B', 'F','F', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'F', 'B', 'F']



def pleaseConformOnepass(caps):
    try:
        caps = caps + [caps[0]]

        last_num = cap2.index(cap2[1], len(cap2) - 3, len(cap2) - 1); print(last_num) # 마지막 모자 뒤집는 index 번호
        last_flip = cap2[last_num]; print(last_flip) # 마지막 모자 뒤집는 type
        index_num = 1; print(index_num)

        for i in range(1, len(caps)):
            if caps[i] != caps[i-1]:
                if caps[i] != caps[0]:
                    if index_num + 1 > last_num:
                        print('People at positions', i, 'flip your caps!')
                        break.
                    else:
                        print('People in positions', i, end='')
                else:
                    print(' through', i-1, 'flip your caps!')
                    
            index_num += 1

    except IndexError as e:
        print("Error :",e)
        print("리스트가 비어있어 인덱싱에 실패했습니다.")

pleaseConformOnepass(cap2)


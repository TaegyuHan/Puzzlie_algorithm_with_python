# -*- coding: utf-8 -*-
""" 
    BIG_ICPC
    순천향대학교 빅데이터공학과
    20171483 한태규
    
    #------------------------- memo -------------------------#
    퍼즐로 배우는 알고리즘 with Python
    
    Page num : 47
    Prac : 1
    #--------------------------------------------------------#
     
    email : gksxorb147@gmail.com
    update : 2021.04.05 13:17
"""


def schedule_table(sched):

    """ 스케줄을 받으면 시간표를 정리해서
        dict형식으로 return 합니다.

    Parameters
    ----------
    sched : list
            스케줄 리스트 
    
     ex ) : [ (6, 8), (6, 12), (6, 7),
              (7, 8), (7, 10), (8, 9),
              (8, 10), (9, 12),(9, 10),
              (10, 11), (10, 12), (11, 12) ]

    Returns
    -------
    schedule_table : dict
            시간표 반환
            { 시간 : 연예인 인원 }

    ex ) : { 6.0: 3, 6.5: 3, 7.0: 4, 7.5: 4,
             8.0: 4, 8.5: 4, 9.0: 5, 9.5: 5,
             10.0: 4, 10.5: 4, 11.0: 4, 11.5: 4, 12.0: 0 }

    """    


    # 연예인 처음 오는시간
    # 마지막에 나가는 시간
    fst = sched[0][0] # 6
    lst = sched[0][1] # 8
    
    # 저장할 시간표 변수
    sched_table = {}

    # print(fst)
    # print(lst)

    ## 연예인이 처음오는시간
    ## 마지막에 가는 시간 찾기
    for in_t, out_t in sched:
        # 첫번째 시간 찾기
        if fst > in_t:
            fst = in_t
        # 마지막 시간 찾기
        if lst < out_t:
            lst = out_t

    # 빈 시간표 table 만들기
    i = 0
    sched_updata = 0
    while (lst - 0.5) > sched_updata:
        sched_updata = (fst + i*0.5)
        i += 1
        sched_table[sched_updata] = 0
        # print(fst + i*0.5)
        
    # 시간표 채워 넣기
    for srt_t, end_t in sched:
        # print(srt_t, end_t)
        i = 0
        sched_updata = 0
        while (end_t - 0.5) > sched_updata:
            sched_updata = (srt_t + i*0.5)
            # print(sched_updata)
            i += 1
            sched_table[sched_updata] += 1
            
    # print(sched_table)
    return sched_table



def find_party_time(sched, srt_t, end_t):

    """ 연예인들의 리스트를 확인 후 가장
        가장 많은 연예인을 만날 수 있는 시간에
        참석하는 연예인을 찾아 그때의 시간과
        연예인 수를 출력합니다.
    

    Returns
    -------
    go_time : int or float
        파티를 참석해야할 가장 최적의 시간
        
    meet_star : int
        최적의 시간에 만나는 연예인 수


    """
    
    ## 최적의 시간을 찾게 도와줄 변수들
    meet_star = 0
    go_time = 0

    ## 스케줄 table 가져오기
    schedule = schedule_table(sched)
    
    # print(sched)
    # print(schedule)
    
        # 빈 시간표 table 만들기
    i = 0
    sched_time = 0
    while (end_t - 0.5) > sched_time:
        sched_time = (srt_t + i*0.5)
        i += 1
        try:
            if meet_star < schedule[sched_time]:
                meet_star = schedule[sched_time]
                go_time = sched_time
        except:
            pass

    print('최적의 시간    > time  : {}'.format(go_time))
    print('입장시간    > time  : {}'.format(int(go_time)))
    print('만나는 연예인  > num   : {}'.format(meet_star))
    print('함수의 반환 값 > go_time : {}, time_star : {}'.format(int(go_time), meet_star))
    
    go_time = int(go_time)
    return go_time, meet_star




if __name__=="__main__":
    
    sched = [ (6, 8), (6, 12), (6, 7),
              (7, 8), (7, 10), (8, 9),
              (8, 10), (9, 12),(9, 10),
              (10, 11), (10, 12), (11, 12) ]

    sched2 = [(6.0, 8.0), (6.5, 12.0), (6.5, 7.0), (7.0, 8.0), (7.5, 10.0), (8.0, 9.0),
              (8.0, 10.0), (9.0, 12.0), (9.5, 10.0), (10.0, 11.0), (10.0, 12.0), (11.0, 12.0)]

    find_party_time(sched2, 1.0, 12.0)
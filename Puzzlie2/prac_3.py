# -*- coding: utf-8 -*-
""" 
    BIG_ICPC
    순천향대학교 빅데이터공학과
    20171483 한태규
    
    #------------------------- memo -------------------------#
    퍼즐로 배우는 알고리즘 with Python
    
    Page num : 48
    Prac : 2
    #--------------------------------------------------------#
     
    email : gksxorb147@gmail.com
    update : 2021.04.05 14:00
"""

def schedule_table(sched):
  
    """ 스케줄을 받으면 시간표를 정리해서
        dict형식으로 return 합니

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

    ex ) : 

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
    for in_t, out_t, _ in sched:
        # 첫번째 시간 찾기
        if fst > in_t:
            fst = in_t
        # 마지막 시간 찾기
        if lst < out_t:
            lst = out_t

    # 빈 시간표 table 만들기
    i = 0
    sched_time = 0
    while (lst - 0.5) > sched_time:
        sched_time = (fst + i*0.5)
        i += 1
        sched_table[sched_time] = [0, 0]
        # print(fst + i*0.5)
        
    # 시간표 채워 넣기
    for srt_t, end_t, like in sched:
        # print(srt_t, end_t)
        i = 0
        sched_time = 0
        while (end_t - 0.5) > sched_time:
            sched_time = (srt_t + i*0.5)
            # print(sched_time)
            i += 1
            sched_table[sched_time][0] += 1
            sched_table[sched_time][1] += like
    
    print('<시간표>')
    print(sched_table)
    print()
    return sched_table




def find_party_time(sched, srt_t, end_t):
    """ 연예인들의 리스트를 확인 후 선호도를
        합쳤을 때 가장 높은 값을 가진 시간을
        출력 합니다.

    Args:
        sched (list)): 스케줄 리스트 입니다.
                       내용에는 파티 참석시간
                       파티를 끝내고 나가는 시간
                       선호도가 들어가있습니다.

        ex ) : [ (6.0, 8.0, 2), (6.5, 12.0, 1), (6.5, 7.0, 2),
               (7.0, 8.0, 2), (7.5, 10.0, 3), (8.0, 9.0, 2),
               (8.0, 10.0, 1), (9.0, 12.0, 2), (9.5, 10.0, 4),
               (10.0, 11.0, 2), (10.0, 12.0, 3), (11.0, 12.0, 7) ]

    Returns
    -------
    go_time : int
        파티를 참석해야할 가장 최적의 시간
        
    meet_star : int
        최적의 시간에 만나는 연예인 수

    """


    ## 스케줄 table 가져오기
    schedule = schedule_table(sched)
    print(schedule)

    # print(sched)
    # print(schedule)

    ## 최적의 시간을 찾게 도와줄 변수들
    meet_star = 0
    preference = 0
    go_time = 0

    for srt_t, _, _ in sched:
        if schedule[srt_t][1] > meet_star:
            meet_star = schedule[srt_t][0]
            preference = schedule[srt_t][1]
            go_time = srt_t

    print('최적의 시간    > time  : {}'.format(go_time))
    print('입장시간    > time  : {}'.format(int(go_time)))
    print('만나는 연예인  > num   : {}'.format(meet_star))
    print('선호도 > point   : {}'.format(preference))
    print('함수의 반환 값 > go_time : {}, meet_star : {}'.format(int(go_time), meet_star))
    
    go_time = int(go_time)
    return go_time, meet_star


if __name__=="__main__":

    sched = [ (6, 8), (6, 12), (6, 7),
              (7, 8), (7, 10), (8, 9),
              (8, 10), (9, 12),(9, 10),
              (10, 11), (10, 12), (11, 12) ]

    sched2 = [ (6.0, 8.0, 2), (6.5, 12.0, 1), (6.5, 7.0, 2),
               (7.0, 8.0, 2), (7.5, 10.0, 3), (8.0, 9.0, 2),
               (8.0, 10.0, 1), (9.0, 12.0, 2), (9.5, 10.0, 4),
               (10.0, 11.0, 2), (10.0, 12.0, 3), (11.0, 12.0, 7) ]
    
    find_party_time(sched2, 1.0, 12.0)


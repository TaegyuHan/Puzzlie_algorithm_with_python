""" 
    BIG_ICPC
    순천향대학교 빅데이터공학과
    20171483 한태규
    
    #------------------------- memo -------------------------#
    퍼즐로 배우는 알고리즘 with Python
    
    Page num : 35
    Prac : 4
    #--------------------------------------------------------#
     
    email : gksxorb147@gmail.com
    update : 2021.03.29 00:19
"""

def encoding(str_text):
    """문자를 받아서 인코딩하는 함수 입니다.

    Args:
        str_text (String): 'BWWWWWBWWWW'

    Returns:
        [String]: '1B5W1B4W'
    """

    tx = str_text
    start_num = 0 # 새로운 시작 문자 개수
    result_text = ''

    for n in range(len(tx)):
        # print(n)
        start_num += 1
        if n != len(tx) - 1: # 마지막 문자 빼고
            if tx[n] != tx[n + 1]: # 앞 의 문자랑 비교
                result_text += str(start_num) + tx[n]; #print(result_text)
                start_num = 0
        else: # 마지막 문자
            if tx[n - 1] == tx[n]: # 뒤의 문자랑 비교
                result_text += str(start_num) + tx[n]; #print(result_text)
            else: # 다르면
                start_num = 1
                result_text += str(start_num) + tx[n]; #print(result_text)

    print(result_text)
    return result_text


def decoding(str_text):
    """문자를 받아서 디코딩하는 함수 입니다.

    Args:
        str_text (String): '1B5W1B4W'

    Returns:
        [String]: 'BWWWWWBWWWW'
    """

    tx = str_text
    result_text = ''

    for n in range(0, len(tx), 2): # 문자열의 번호 부분만 추출
        result_text += int(tx[n]) * tx[n + 1]
    
    print(result_text)
    return result_text


if __name__=="__main__":
    encoding('BWWWWWBWWWW')
    decoding('1B5W1B4W')

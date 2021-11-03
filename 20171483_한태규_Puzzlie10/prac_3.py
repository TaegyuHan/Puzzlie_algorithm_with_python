from sys import stdin as I

def check_text(_str):
    # print(f"_str : {_str}")
    sl = len(_str)
    # print(f"len(_str) : {len(_str)}")

    if sl <= 1:
        return True

    if _str[0].lower() != _str[-1].lower():
        return False

    return check_text(_str[1:(sl - 1)])

if __name__ == '__main__':
    I = open("./prac_3.txt")
    text = I.readline()
    text.lower()
    # print(type(text))
    if check_text(text):
        print(f"{text}는 회문 입니다.")
    else:
        print(f"{text}는 회문이 아닙니다.")
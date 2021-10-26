
def noConflicts(board, current):
    """ 현재의 Queen 위치에 놓을 수 있는지 확인합니다.

    :param board: 체스판
    :param current: 현재 Queen을 놓을 세로 칸
    :return: 가능 or 불가능
    """
    for i in range(current):
        if board[i] == board[current]: # 가로 확인
            return False
        if (current - i) == abs(board[current] - board[i]): # 대각선 확인
            return False
    return True

def rQueens(board, current, size):
    """ Queen의 말을 놓습니다.

    :param board: 체스판
    :paam current: 현재 Queen을 놓을 세로 칸
    :param size: 체스판 크기
    """
    if current == size:
        return True
    else:
        for i in range(size):
            board[current] = i
            if noConflicts(board, current):
                found = rQueens(board, current + 1, size)
                if found:
                    return True
        return False

def nQueens(N):
    board = [-1] * N
    rQueens(board, 0, N)
    print(board)

if __name__ == '__main__':
    nQueens(4)
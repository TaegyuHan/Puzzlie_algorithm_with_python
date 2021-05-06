def noConflicts(board, current, qindex, n = 4):

    #check that the row on which the current queen is only has one queen on it
    for j in range(current):
        if board[qindex][j] == 1:
            return False

    #Check the two diagonals from the current queen
    #The first loop is for the diagonal /
    #The second loop is for the diagonal \
    k = 1
    while qindex - k >= 0 and current - k >= 0:
        if board[qindex - k][current - k] == 1:
            return False
        k += 1

    k = 1
    while qindex + k < n and current - k >= 0:
        if board[qindex + k][current - k] == 1:
            return False
        k += 1

    return True 


def FourQueens(n=4):

    #Initialize the board to be empty
    board = [ [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]  ]

    #Place a queen a column at a time beginning with leftmost column
    num = 1
    for i in range(n):
        board[i][0] = 1
        for_loop(num, board)
        board[i][0] = 0

# 무한 loop 문
def for_loop(num, board, n=4):
    if num==4:
        show_board(board)
        num -=1
        return

    for i in range(n):
        board[i][num] = 1
        if noConflicts(board, num, i, n):
            for_loop(num+1, board)
        board[i][num] = 0

def show_board(board):
    
    for row in board:
        for i in row:
            print(i, end=' ')
        print()
    print()

if __name__ == '__main__':
    FourQueens()
    






#Programming for the Puzzled -- Srini Devadas
#Keep Those Queens Apart
#Given a 8 x 8 chess board, figure out how to place 8 Queens such that
#no Queen attacks another queen.
#This code uses a single-dimensional list to represent Queen positions


#This procedure checks that the most recently placed queen on the board on column
#current does not conflict with existing queens.
def noConflicts(board, current):
    for i in range(current):
        # 1자 충돌 확인
        if (board[i] == board[current]):
            return False
        # 대각선 충돌 확인
        # 1-0 == 
        if (current - i == abs(board[current] - board[i])):
            return False
    return True 


#This procedure places 8 Queens on a board so they don't conflict.
#It assumes n = 8 and won't work with other n!
def EightQueens(input_board, n=8):
  
    board = [-1] * n
    print(board)
    queens_num = n - input_board.count(-1)
    print(queens_num)

    #print(queens_num)
    for i in range(n):

        # i = 0, 1, 2, 3, 4, 5, 6, 7
        board[0] = i

        for j in range(n):
            # j = 0, 1, 2, 3, 4, 5, 6, 7
            board[1] = j

            if not noConflicts(board, 1):
                continue
            for k in range(n):
                board[2] = k
                if not noConflicts(board, 2):
                    continue
                for l in range(n):
                    board[3] = l
                    if not noConflicts(board, 3):
                        continue
                    for m in range(n):
                        board[4] = m
                        if not noConflicts(board, 4):
                            continue
                        for o in range(n):
                            board[5] = o
                            if not noConflicts(board, 5):
                                continue
                            for p in range(n):
                                board[6] = p
                                if not noConflicts(board, 6):
                                    continue
                                for q in range(n):
                                    board[7] = q
                                    if noConflicts(board, 7):
                                        # print(board)

                                        # 추가
                                        print(board)
                                        queens_position_num = 0
                                        for r in range(n):
                                            if board[r] == input_board[r]:
                                                queens_position_num += 1
                                        if queens_position_num == queens_num:
                                            print(board)
                                            print(input_board)
    return

if __name__ == '__main__':

    board = [6, 4, 2, -1, -1, -1, -1, -1]
    EightQueens(board)

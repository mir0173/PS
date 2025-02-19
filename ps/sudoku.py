#2239
from sys import stdin
input = stdin.readline

def Row(r, num, board):
    for c in range(9):
        if board[r][c] == num:
            return False
    return True

def Col(c, num, board):
    for r in range(9):
        if board[r][c] == num:
            return False
    return True

def Small(r, c, num, board):
    r_num = (r // 3) * 3
    c_num = (c // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[r_num + i][c_num + j] == num:
                return False
    return True

def print_board(depth, zero, board):
    if depth == len(zero):
        for row in range(9):
            for col in range(9):
                print(board[row][col], end="")
            print()
        exit()

    r_num, c_num = zero[depth]  
    for num in range(1, 10):
        if Row(r_num, num, board) and Col(c_num, num, board) and Small(r_num, c_num, num, board):
            board[r_num][c_num] = num
            print_board(depth + 1, zero, board)
            board[r_num][c_num] = 0

def main():
    board = []
    zero = []
    for r in range(9):
        board.append(list(map(int, input().rstrip())))
        for c in range(9):
            if board[r][c] == 0:
                zero.append((r, c))
    print_board(0, zero, board)

if __name__ == '__main__':
    main()
"""
dcp#64

This problem was asked by Google.

A knight's tour is a sequence of moves by a knight on a chessboard such that all squares are visited once.

Given N, write a function to return the number of knight's tours on an N by N chessboard.

"""

"""
https://en.wikipedia.org/wiki/Knight%27s_tour

n - # directed tours (open and closed)
--------------------------------------
1 - 1
2 - 0
3 - 0
4 - 0
5 - 1728
6 - 6,637,920
7 - 165,575,218,320
8 - 19,591,828,170,979,904

The # of undirected tours is half the number of directed tours.

"""



# These define how a knight can move
x_move = [2, 1, -1, -2, -2, -1,  1,  2]
y_move = [1, 2,  2,  1, -1, -2, -2, -1]

  
def is_safe(board, x, y):
    n = len(board)
    return (x >= 0 and x < n and y >= 0 and y < n and board[x][y] == '')


def print_board(board):
    n = len(board)

    for r in range(0, n):
        for c in range(0, n):
            print("{:3}".format(board[r][c]), end=' ')

        print()

    print()


#import copy

def knight_tours_util(board, solutions, x, y, move_num):
    if move_num == len(board)**2:
        board_copy = [row[:] for row in board]
        #board_copy = copy.deepcopy(board)
        solutions.append(board_copy)
        return

   # Try all next moves from the current coordinates x, y

    for k in range(0, 8):
        next_x = x + x_move[k]
        next_y = y + y_move[k]

        if is_safe(board, next_x, next_y):
            board[next_x][next_y] = move_num
            knight_tours_util(board, solutions, next_x, next_y, move_num + 1)
            board[next_x][next_y] = '' # backtracking 


def knight_tours(n, x_start=0, y_start=0):
    board = [['']*n for _ in range(0, n)]

    # Let knight be in upper-left block at start
    board[x_start][y_start] = 0

    solutions = []

    knight_tours_util(board, solutions, x_start, y_start, 1)
  
    return solutions


def num_knight_tours(n):
    num_solutions_board = [[0]*n for _ in range(0, n)]

    for x in range(0, n):
        for y in range(0, n):
            num_solutions_board[x][y] = len(knight_tours(n, x, y))

    return num_solutions_board


# very slow if n >= 6
n = 5
print("n = {}".format(n))

# x = 0
# y = 0
# solutions = knight_tours(n, x, y)

# for s in solutions:
#     print_board(s)

# num = len(solutions)
# print("number of knight's tours from position ({}, {}) = {}".format(x, y, num))


num_solutions_board = num_knight_tours(n)
print_board(num_solutions_board)
num_solutions = sum(map(sum, num_solutions_board)) # sum of 2d matrix
print("total number of knight's tours across all starting positions = {}".format(num_solutions))

"""
304   0  56   0 304
  0  56   0  56   0
 56   0  64   0  56
  0  56   0  56   0
304   0  56   0 304

n = 5
total number of knight's tours across all starting positions = 1728
"""


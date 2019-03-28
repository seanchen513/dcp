"""
dcp#38 

This problem was asked by Microsoft.

You have an N by N board. Write a function that, given N, returns the number of possible arrangements of the board where N queens can be placed on the board without threatening each other, i.e. no two queens share the same row, column, or diagonal.

"""


# Return False if there is any conflict between the queen
# that would be placed at (row, col) and any other queen. 
# Assume queens are placed one at a time row-wise starting with first row.
# So only need to check portion of board above variable "row".
# Don't need to check along "row" itself.
def is_safe(board, row, col):
    n = len(board[0])

    # check along col
    for r in range(0, row):
        if board[r][col] == 1:
            return False

    # check along main diagonal to upper-left of (row,col)
    for r,c in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[r][c] == 1:
            return False

    # check along off-diagonal to upper-right of (row,col)
    for r,c in zip(range(row-1, -1, -1), range(col+1, n, 1)):
        if board[r][c] == 1:
            return False

    return True

#import copy

def queens(board, solutions, row=0):
    n = len(board[0])

    if row >= n:
        board_copy = [row[:] for row in board]
        #board_copy = copy.deepcopy(board)
        solutions.append(board_copy)
        
        return board

    for col in range(0, n):
        if is_safe(board, row, col):
            board[row][col] = 1
            queens(board, solutions, row+1)
            board[row][col] = 0


def find_solutions(n):
    board = [[0] * n for _ in range(0,n)]

    solutions = []
    queens(board, solutions)
    return solutions


def num_solutions(n):
    solutions = find_solutions(n)
    return len(solutions)


def print_all_solutions(n):
    board = [[0] * n for _ in range(0,n)]

    solutions = []
    queens(board, solutions)

    print("\nn = {}".format(n))    
    print("# solutions = {}\n".format(len(solutions)))

    for s in solutions:
        print_board(s)
        print()


def print_board(board):
    for row in range(0,len(board)):
        for col in range(0,len(board[0])):
            print(board[row][col], end=' ')

        print()


"""
https://en.wikipedia.org/wiki/Eight_queens_puzzle

n = 1 # 1 solution
n = 2 # no solution
n = 3 # no solution
n = 4 # 2 solutions
n = 5 # 10 solutions
n = 6 # 4 solutions
n = 7 # 40 solutions
n = 8 # 92 solutions
n = 9 # 352 solutions
n = 10 # 724 solutions
...
n = 24 # 227,514,171,973,736 solutions
"""

for n in range(1, 11):
    n_sol = num_solutions(n)
    print("n = {}\t# solutions = {}".format(n, n_sol))

print("="*80)
print_all_solutions(6)


"""
dcp#122

This question was asked by Zillow.

You are given a 2-d matrix where each cell represents number of coins in that cell. Assuming we start at matrix[0][0], and can only move right or down, find the maximum number of coins you can collect by the bottom right corner.

For example, in this matrix

0 3 1 1
2 0 0 4
1 5 3 1
The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.

"""

"""
max_sums for example given in problem:
0 3  4  5
2 3  4  9
3 8 11 12
"""

import copy

"""
Sums up to each cell are path-dependent.

Notation: max_sum(r, c) is the maximum sum among all paths from upper left corner 
of matrix m to cell at row r and column c in the matrix.

Base case: For each cell in first row or first column, there is exactly one path to that cell.
So we can calculate the max sum among paths to each of those cells.

Induction step: Assume we are at cell (r, c) not in the first row or first column,
and that we have calculated max sums among all paths for the cell above it (r-1, c) 
and the cell to the left of it (r, c-1).  Then
max_sum(r, c) = max[ max_sum(r-1, c), max_sum(r, c-1) ] + m(r,c)
"""
def find_max_sums(matrix):
    m = copy.deepcopy(matrix) # so we don't modify matrix argument
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    for i in range(1, num_rows):
        m[i][0] = m[i-1][0] + matrix[i][0]

    for j in range(1, num_cols):
        m[0][j] = m[0][j-1] + matrix[0][j]

    for i in range(1, num_rows):
        for j in range(1, num_cols):
            m[i][j] = max(m[i-1][j], m[i][j-1]) + matrix[i][j]

    return m


def find_max_sum_recursive(matrix, r, c):
    if r == 0:
        if c == 0:
            return matrix[0][0]
        else:
            return matrix[0][c] + find_max_sum_recursive(matrix, 0, c-1)

    elif c == 0:
        return matrix[r][0] + find_max_sum_recursive(matrix, r-1, 0)

    return max(find_max_sum_recursive(matrix, r-1, c),
        find_max_sum_recursive(matrix, r, c-1) ) + matrix[r][c]


def print_matrix(m):
    n_rows = len(m)
    n_cols = len(m[0])

    for i in range(n_rows):
        for j in range(n_cols):
            print("{:5}".format(m[i][j]), end='')

        print()


###############################################################################

matrix = [
    [0, 3, 1, 1], 
    [2, 0, 0, 4], 
    [1, 5, 3, 1]]

max_sums = find_max_sums(matrix)
max_sum = max_sums[-1][-1] # lower right corner

print("\nmatrix:")
print_matrix(matrix)

print("\nmax_sums:")
print_matrix(max_sums)

print("\nmax sum among all paths from upper left to lower right corner = ")
print(max_sum)

num_rows = len(matrix)
num_cols = len(matrix[0])
max_sum = find_max_sum_recursive(matrix, num_rows-1, num_cols-1)

print("\nsame thing calculated recursively = ")
print(max_sum)


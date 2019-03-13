"""
dcp#158

This problem was asked by Slack.

You are given an N by M matrix of 0s and 1s. Starting from the top left corner, how many ways are there to reach the bottom right corner?

You can only move right and down. 0 represents an empty space while 1 represents a wall you cannot walk through.

For example, given the following matrix:

[[0, 0, 1],
 [0, 0, 1],
 [1, 0, 0]]

Return two, as there are only two ways to get to the bottom right:

    Right, down, down, right
    Down, right, down, right

The top left corner and bottom right corner will always be 0.
"""


# iterative solution
def n_paths_matrix(matrix):
    n_rows = len(matrix)
    n_cols = len(matrix[0])

    # will store number of paths from upper left corner to current cell
    n_paths = [[0]*n_cols for _ in range(n_rows)]

    # initialize 1st column of n_paths
    for i in range(0, n_rows):
        if matrix[i][0] != 0:
            break
        
        n_paths[i][0] = 1
        
    # initialize 1st row of n_paths
    for j in range(0, n_cols):
        if matrix[0][j] != 0:
            break

        n_paths[0][j] = 1

    # calculate n_paths for rest of matrix
    for i in range(1, n_rows):
        for j in range(1, n_cols):
            if matrix[i][j] == 1:
                n_paths[i][j] = 0
            else:
                n_paths[i][j] = n_paths[i-1][j] + n_paths[i][j-1]

    return n_paths


def count_paths(matrix):
    n_paths = n_paths_matrix(matrix)
    return n_paths[-1][-1]


# recursive solution
# assume row and col are non-negative integers
def count_paths_r(matrix, row, col):
    if (row == 0) and (col == 0):
        return 1 - matrix[0][0]

    if row == 0:
        return count_paths_r(matrix, row, col - 1)

    if col == 0:
        return count_paths_r(matrix, row - 1, col)

    n_paths_from_above = 0
    n_paths_from_left = 0
    
    if matrix[row-1][col] == 0:
        n_paths_from_above = count_paths_r(matrix, row - 1, col)
        
    if matrix[row][col-1] == 0:
        n_paths_from_left = count_paths_r(matrix, row, col - 1)

    return n_paths_from_above + n_paths_from_left


def print_matrix(matrix):
    n_rows = len(matrix)
    n_cols = len(matrix[0])

    for i in range(0, n_rows):
        for j in range(0, n_cols):
            print(matrix[i][j], end=' ')

        print()


matrix = [[0,0,1,0,0]]

matrix = [[0], [0], [1], [0], [0]]

matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]

matrix = [
    [0, 0, 1],
    [0, 0, 1],
    [1, 0, 0]]

n_paths = n_paths_matrix(matrix)
n = count_paths(matrix)
n_recursive = count_paths_r(matrix, len(matrix)-1, len(matrix[0])-1)

print("\noriginal matrix:")
print_matrix(matrix)

print("\nn_paths matrix:")
print_matrix(n_paths)

print("\nnumber of paths from upper left to lower right corner = {}".format(n))
print("\nnumber of paths from upper left to lower right corner (recursive sol) = {}".format(n_recursive))


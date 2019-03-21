"""
dcp#168

This problem was asked by Facebook.

Given an N by N matrix, rotate it by 90 degrees clockwise.

For example, given the following matrix:

[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]

you should return:

[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]

Follow-up: What if you couldn't use any extra space?
"""

# Clarify: can we use O(1) extra space?


# using a lot of extra space (returns new matrix of same size)
def rotate_ccw(m):
    n = len(m)
    r = []

    for col in range(n-1, -1, -1):
        lst = []

        for row in range(0, n):
            lst.append(m[row][col])

        r.append(lst)

    return r


# using a lot of extra space (returns new matrix of same size)
def rotate_cw(m):
    n = len(m)
    r = []

    for col in range(0, n):
        lst = []

        for row in range(n-1, -1, -1):
            lst.append(m[row][col])

        r.append(lst)

    return r


"""
(0, 0) ... (0, k)
.           .
.           .
(k, 0) ... (k, k)


*** following diagram is rotated, but shows which cells go together:
(d, k) ...      (k, n-1 - d)
.               .
.               .
(n-1 - k, d) ... (d, n-1 - k)
"""

# O(1) extra space
def rotate(m):
    n = len(m)
    depth = n // 2

    for d in range(0, depth):
        for k in range(d, n-1 - d):
            temp = m[d][k]
            m[d][k] = m[n-1 - k][d]
            m[n-1 - k][d] = m[n-1 - d][n-1 - k]
            m[n-1 - d][n-1 - k] = m[k][n-1 - d]
            m[k][n-1 - d] = temp

    return m


def print_matrix(m):
    for i in range(0, len(m)):
        for j in range(0, len(m[0])):
            print("{:3}".format(m[i][j]), end=' ')
        print()


matrix = [[1]]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

matrix = [
    [ 1,  2,  3,  4],
    [ 5,  6,  7,  8],
    [ 9, 10, 11, 12],
    [13, 14, 15, 16]]

print("\nmatrix:")
print_matrix(matrix)

matrix2 = rotate_cw(matrix)
print("\nOriginal matrix after 90 degrees clockwise rotation (using extra space):")
print_matrix(matrix2)

rotate(matrix)
print("\nOriginal matrix after 90 degrees clockwise rotation (one extra var):")
print_matrix(matrix)

rotate(matrix)
rotate(matrix)
rotate(matrix)
print("\nOriginal matrix after 4 total rotations CW (one extra var):")
print_matrix(matrix)


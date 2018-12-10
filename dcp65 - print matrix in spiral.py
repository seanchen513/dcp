'''
dcp#65

This problem was asked by Amazon.

Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
You should print out the following:

1
2
3
4
5
10
15
20
19
18
17
16
11
6
7
8
9
14
13
12
'''

# this link not really referred to in my solutions:
# https://stackoverflow.com/questions/726756/print-two-dimensional-array-in-spiral-order

# solution is O(mn)



def print_matrix(a):
    for i in range(0,len(a)):
        for j in range(0,len(a[0])):
            print(a[i][j], end=' ')
        print()

# NEED TO FIX
# doesn't work in all cases
def print_spiral(a):
    n = len(a)
    m = len(a[0])

    if n == 1:
        for j in range(0, m):
            print(a[0][j])
        return

    if m == 1:
        for i in range(0, n):
            print(a[i][0])
        return

    d_max = min(n, m) - 2
    print("n = {}".format(n))
    print("m = {}".format(m))
    print("d_max = {}".format(d_max))

    for d in range(0, d_max+1):
        print("-"*20)

        m_max = (m - 1) - d
        n_max = (n - 1) - d

        for j in range(d, m_max):
            print("i,j = {},{}: ".format(d, j), end=" ")
            print(a[d][j])
        
        print("-"*20)
        for i in range(d, n_max):
            print("i,j = {},{}: ".format(i, m_max), end=" ")
            print(a[i][m_max])

        print("-"*20)
        for j in range(m_max, d, -1):
            print("i,j = {},{}: ".format(n_max, j), end=" ")
            print(a[n_max][j])

        print("-"*20)
        for i in range(n_max, d, -1):
            print("i,j = {},{}: ".format(i, d), end=" ")
            print(a[i][d])

# https://www.geeksforgeeks.org/print-a-given-matrix-in-spiral-form/
# go straight until hit barrier
def print_spiral2(a):
    n = len(a)
    m = len(a[0])
    d_max = min(n, m) - 1
    print("n = {}".format(n))
    print("m = {}".format(m))
    print("d_max = {}".format(d_max))

    row_start = 0
    row_end = n - 1

    col_start = 0
    col_end = m - 1

    while (row_start <= row_end and col_start <= col_end):
        print("-"*20)
        for j in range(col_start, col_end + 1):
            print(a[row_start][j])
        
        row_start += 1
        print("-"*20)

        for i in range(row_start, row_end + 1):
            print(a[i][col_end])

        col_end -= 1
        print("-"*20)

        if row_start <= row_end:
            for j in range(col_end, col_start - 1, -1):
                print(a[row_end][j])

            row_end -= 1
            print("-"*20)

        if col_start <= col_end:
            for i in range(row_end, row_start - 1, -1):
                print(a[i][col_start])

            col_start += 1


# 4x5 matrix
a = [[1,  2,  3,  4,  5],
    [6,  7,  8,  9,  10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]]
print_matrix(a)
print_spiral2(a)

# square matrix
a = [[1,  2,  3,  4,  5],
    [6,  7,  8,  9,  10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]]

# 1x1 matrix
a = [[1]]

# row matrix
a = [[1,2,3,4,5]]

# column matrix
a = [[1],[2],[3],[4],[5]]

# 2x5 matrix
a = [[1,  2,  3,  4,  5],
    [6,  7,  8,  9,  10]]

# 5x2 matrix
a = [[1,2],[3,4],[5,6],[7,8],[9,10]]



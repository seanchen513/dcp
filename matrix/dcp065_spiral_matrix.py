"""
dcp65

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
"""

"""
LC54. Spiral Matrix
Medium

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
"""

def print_matrix(a):
    if not a:
        return

    for i in range(len(a)):
        for j in range(len(a[0])):
            print(f"{a[i][j]:3}", end=' ')

        print()

"""
Solution for dcp65.
Same as solution for LeetCode, but print things out rather than returning
result.  Kept this to have other print statements for debugging and
learning purposes.
"""
def print_spiral2(a):
    #if (a is None) or (len(a) == 0):
    if not a:
        return

    top = 0
    bottom = len(a) - 1

    left = 0
    right = len(a[0]) - 1
    
    print("#"*20)

    while (left <= right) and (top <= bottom):
        for i in range(left, right + 1):
            print(a[top][i])
        
        top += 1
        print("#"*20)

        for i in range(top, bottom + 1):
            print(a[i][right])

        right -= 1
        print("#"*20)
        
        if top <= bottom:
            for i in range(right, left - 1, -1):
                print(a[bottom][i])

            bottom -= 1
            print("#"*20)

        if left <= right:
            for i in range(bottom, top - 1, -1):
                print(a[i][left])
            
            left += 1
            print("#"*20)

###############################################################################
"""
Solution #1:

a = [None] # error... but LeetCode doesn't check this

O(n) time, where n = total number of elements in matrix
O(n) space due to answer matrix

LeetCode Jan 19, 2020:
Runtime: 24 ms, faster than 86.62% of Python3 online submissions for Spiral Matrix.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Spiral Matrix.
"""
def spiral_order(a):
    if not a:
        return []
    
    top = 0
    bottom = len(a) - 1

    left = 0
    right = len(a[0]) - 1

    spiral = []

    while (left <= right) and (top <= bottom):
        for i in range(left, right + 1):
            spiral.append(a[top][i])
        
        top += 1
        
        for i in range(top, bottom + 1):
            spiral.append(a[i][right])
        
        right -= 1
    
        # "top" was just modified, so need to check
        if top <= bottom:
            for i in range(right, left - 1, -1):
                spiral.append(a[bottom][i])
        
            bottom -= 1

        # "right" was just modified, so need to check
        if left <= right:    
            for i in range(bottom, top - 1, -1):
                spiral.append(a[i][left])
                        
            left += 1
    
    return spiral

###############################################################################

"""
Solution #2: same as sol #1, but use list extend() method instead of
using "for" loops with list append().  This is faster.

Runtime: 20 ms, faster than 96.83% of Python3 online submissions for Spiral Matrix.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Spiral Matrix.
"""
def spiral_order2(a):
    if not a:
        return []
    
    top = 0
    bottom = len(a) - 1

    left = 0
    right = len(a[0]) - 1

    spiral = []

    while (left <= right) and (top <= bottom):       
        #spiral.extend(a[top][left:right+1])
        spiral.extend(a[top][i] for i in range(left, right + 1))
        top += 1
        
        spiral.extend(a[i][right] for i in range(top, bottom+1))
        right -= 1
    
        # "top" was just modified, so need to check
        if top <= bottom:
            #spiral.extend(a[bottom][right:(left-1):-1]) # doesn't work?
            spiral.extend(a[bottom][i] for i in range(right, left - 1, -1))
            bottom -= 1

        # "right" was just modified, so need to check
        if left <= right:    
            spiral.extend(a[i][left] for i in range(bottom, top - 1, -1))
            left += 1
    
    return spiral

###############################################################################
"""
Based on LC sol #1.
Slow and takes up more space.

O(n) time, where n = total number of elements in matrix
O(n) space due to answer and seen matrices
"""
def spiral_order3(a):
    if not a: 
        return []

    R, C = len(a), len(a[0])
    seen = [[False] * C for _ in a]
    ans = []

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    r = c = di = 0

    for _ in range(R * C):
        ans.append(a[r][c])
        seen[r][c] = True
        cr, cc = r + dr[di], c + dc[di]

        if (0 <= cr < R) and (0 <= cc < C) and (not seen[cr][cc]):
            r, c = cr, cc
        else:
            di = (di + 1) % 4
            r, c = r + dr[di], c + dc[di]

    return ans

###############################################################################

if __name__ == "__main__":
    # 4x5 matrix
    b = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

    # 5x5 square matrix
    a = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]]

    a = [[1]] # 1x1

    a = [[1,2,3,4,5]] # 1x5 row matrix
    a = [[1],[2],[3],[4],[5]] # 5x1 column matrix

    a = [[1,2,3,4,5], [6,7,8,9,10]] # 2x5
    a = [[1,2],[3,4],[5,6],[7,8],[9,10]] # 5x2
    a = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]] # 5x3
    a = [[1,2,3,4],[5,6,7,8],[9,10,11,12]] # 3x4

    ###

    #a = [] # return []
    #a = None # return []
    #a = [[]] # return []
    #a = [[], []] # return []
    #a = [None] # error... but LeetCode doesn't check this

    print_matrix(a)
    #print_spiral2(a)
    print_spiral2(a)

    spiral = spiral_order(a)
    spiral2 = spiral_order2(a)
    spiral3 = spiral_order3(a)
    print(spiral)
    print(spiral2)
    print(spiral3)

    ###
    """
    import timeit

    t1 = timeit.timeit("spiral = spiral_order(b)", "from __main__ import spiral_order, b", number=1000)
    t2 = timeit.timeit("spiral = spiral_order2(b)", "from __main__ import spiral_order2, b", number=1000)
    t3 = timeit.timeit("spiral = spiral_order3(b)", "from __main__ import spiral_order3, b", number=1000)

    print(f"\nt1  = {t1}")
    print(f"\nt2  = {t2}")
    print(f"\nt3  = {t3}")
    """

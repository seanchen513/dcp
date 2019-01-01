"""
This problem was asked by Facebook.

There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner. You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

Right, then down
Down, then right

Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.
"""

import math

# recursive solution

def num_ways(n, m):
    if n == 1 or m == 1:
        return 1
    
    return num_ways(n-1, m) + num_ways(n, m-1)


# solution using dynamic programming, tabular or bottom-up approach

def num_ways2(n, m):
    count = [[0]*m for i in range(n)]

    for i in range(n):
        count[i][0] = 1

    for j in range(m):
        count[0][j] = 1

    for i in range(1, n):
        for j in range(1, m):
            count[i][j] = count[i-1][j] + count[i][j-1]

    return count[n-1][m-1]

# Mathematical solution:
# n-1 moves down
# m-1 moves to right
# How many ways are there to choose n+m-2 moves, where n-1 moves are down and m-1 moves are to right
# and where order matters?
# Answer: C(n+m-2, n-1) = C(n+m-2, m-1)

# assume n and m are positive integers
def num_ways3(n, m):
    return int(math.factorial(n+m-2)/math.factorial(n-1)/math.factorial(m-1))

def compare(n, m):
    print()
    print("{}x{}: num ways (recursive)= {}".format(n, m, num_ways(n, m)) )
    print("{}x{}: num ways (tabular)= {}".format(n, m, num_ways2(n, m)) )
    print("{}x{}: num ways (math)= {}".format(n, m, num_ways3(n, m)) )


compare(1, 1) # 1
compare(5, 1) # 1
compare(1, 5) # 1
compare(2, 2) # 2
compare(5, 5) # 70
compare(5, 8) # 330



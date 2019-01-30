"""
dcp#101

This problem was asked by Alibaba.

Given an even number (greater than 2), return two prime numbers whose sum will be equal to the given number.

A solution will always exist. See Goldbach’s conjecture.

Example:

Input: 4
Output: 2 + 2 = 4
If there are more than one solution possible, return the lexicographically smaller solution.

If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, then

[a, b] < [c, d]
If a < c OR a==c AND b < d.

"""

import math


# Every prime > 3 has form 6k-1 or 6k+1
def is_prime(n):
    if n < 2:
        return None

    if n == 2 or n == 3:
        return True

    if (n % 2 == 0) or (n % 3 == 0):
        return False

    d = 5
    n_sqrt = int(math.sqrt(n)) + 1

    while d <= n_sqrt:
        # might do an extraneous comparison for d+2 > n_sqrt
        if (n % d == 0) or (n % (d+2) == 0):
            return False
            
        d += 6        

    return True


# assume n is integer >= 4
def goldbach(n):
    last = int(n/2) + 1

    for k in range(2, last):
        if not is_prime(k):
            continue
        
        if not is_prime(n - k):
            continue
        
        return k


n = 100 # 3 + 97
n = 1024 # 3 + 1021

n = 999999998 # 61 + 999999937
n = 9999999998 # 31 + 9999999967
n = 99999999998 # 21 + 99999999977
n = 100000000001 # 24 + 99999999977 # not even
n = 100000000000 # 23 + 99999999977

n = 4 # 2 + 2
n = 6 # 3 + 3
n = 8 # 3 + 5
n = 10 # 3 + 7
n = 12 # 5 + 7
n = 14 # 3 + 11
n = 16 # 3 + 13
n = 18 # 5 + 13
n = 20 # 3 + 17
n = 22 # 3 + 19

"""
g = goldbach(n)

print("n = {}".format(n))
print("goldbach = {} + {}".format(g, n - g))
"""

for n in range(4, 101, 2):
    g = goldbach(n)
    print("{} = {} + {}".format(n, g, n-g))






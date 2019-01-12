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

# assume n is integer >= 2
def is_prime(n):
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    last = int(math.sqrt(n)) + 1

    # k: 3, 5, 7, 9 (not prime), 11, 13, 15 (not prime), 
    # 17, 19, 21 (not prime), 23, 25 (not prime), 27 (not prime),
    # 29, 31, 33 (not prime), 35 (not prime), 37, 39 (not prime),
    # 41, 43, 45 (not prime), 47, 49 (not prime), ...
    for k in range(3, last, 2): 
        if n % k == 0:
            return False

    return True


# assume n is integer >= 4
def goldbach(n):
    last = int(n/2) + 1

    for k in range(2, last):
        if not is_prime(2):
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

g = goldbach(n)

print("n = {}".format(n))
print("goldbach = {} + {}".format(g, n - g))




"""
dcp#221

This problem was asked by Zillow.

Let's define a "sevenish" number to be one which is either a power of 7, or the sum of unique powers of 7. The first few sevenish numbers are 1, 7, 8, 49, and so on. Create an algorithm to find the nth sevenish number.
"""

"""
n                        powers of 7     # diff sums     bit pattern of powers of 7
1    1   7^0             0               1 = 2^0         1

2    7   7^1             1               2 = 2^1         10
3    8   1 + 7           1, 0                            11

4    49  7^2             2               4 = 2^2         100
5    50  49 + 1          2, 0                            101
6    56  49 + 7          2, 1                            110
7    57  49 + 7 + 1      2, 1, 0                         111

8    343     7^3         3               8 = 2^3         1000
9    344                 3, 0                            1001
10   350                 3, 1                            1010
11   351                 3, 1, 0                         1011
12                       3, 2                            1100
13                       3, 2, 0                         1101
14                       3, 2, 1                         1110
15                       3, 2, 1, 0                      1111


#(set of sums including kth power of 7) = 2^(highest power of 7 in set of sums)

Let n be given.
Let p = floor(log_2 n)
....
"""

# Given n is decimal reprensentation of a positive integer.
# Interpret binary bits of n with base 7.
def seven_rep(n):
    sum = 0
    k = 0

    while n > 0:
        sum += (n & 1) * (7 ** k)
        n = n >> 1
        k += 1

    return sum


for n in range(1, 30):
    k = seven_rep(n)
    print("n = {}, its 7-rep is {}".format(n, k))


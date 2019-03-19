"""
dcp#9

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""

# Clarify if we can make these assumptions:
# Assume list has at least 3 elements.
# Assume by "list", we can use Python list.


# Naive solution
# Oops, this is for sum of 2 elements only.
def largest_sum_of_two_non_adjacent(a):
    n = len(a)
    max_sum = a[0] + a[2]

    for i in range(0, n):
        for j in range(0, i - 1):
            max_sum = max(max_sum, a[i] + a[j])

        for j in range(i + 1, n):
            max_sum = max(max_sum, a[i] + a[j])

    return max_sum


# Solution using bits
# Assume we can take sum of no elements, whose sum is 0.
# Two adjacent bits of x are set if x & (x >> 1) != 0
def largest_sum_non_adjacent(a):
    # number of bits to use = number of elements in a
    n = len(a)

    max_sum = 0

    for i in range(0, 2**n): # loop through power set of a
        if i & (i >> 1): # adjacent bits are set
            continue

        sum = 0
        for k in range(0, n):
            if i & (1 << k):
                sum += a[k]
        
        max_sum = max(max_sum, sum)

    return max_sum


# https://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/
# https://stackoverflow.com/questions/4487438/maximum-sum-of-non-consecutive-elements


# Assume input array/list has at least one element, and that sums must take at least one element.
# Dynamic programming
# Let m(i) = max sum for a[0] through a[i].
# Then m(i) = max{ m(i-1), m(i-2) + a[i] }
# Base case: m(0) = a[0].  Define m(-1) = 0. 
# m(1) = max( m(0), m(-1) + a[1] ) = max( m(0) = a[0], a[1] )
def largest_sum_non_adjacent2(a):
    m = {}
    m[-1] = 0
    m[0] = a[0]
 
    for i in range(1, len(a)):
        m[i] = max( m[i-1], m[i-2] + a[i] )

    return m[len(a)-1]


a = [] # 0
a = [23] # 23
a = [-5] # 0 if we can take sum of no elements; otherwise -5
a = [5, 1, 1, 5] # 10
a = [2, 4, 6, 2, 5] # 13

s = largest_sum_non_adjacent(a)
s = largest_sum_non_adjacent2(a)

print("a = {}".format(a))
print("largest sum of non-adjacent ints (bits) = {}".format(s))
print("largest sum of non-adjacent ints (DP)   = {}".format(s))


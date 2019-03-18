"""
dcp#164

This problem was asked by Google.

You are given an array of length n + 1 whose elements belong to the set {1, 2, ..., n}. By the pigeonhole principle, there must be a duplicate. Find it in linear time and space.
"""

# Naive solution: nested loops, O(n^2) time, O(1) space
# Solution: Sorting and then looking for equal, adjacent elements is O(n log n) time.

import random

# Solution #1: use hash table (Python set)
# O(n) time, O(n) space
def find_duplicate(a):
    found = set()

    for x in a:
        if x not in found:
            found.add(x)
        else:
            return x


# Solution #2: Each of 1, 2, ..., n appears exactly once; sum of these is n*(n+1)/2.
# O(n) time, O(1) space
def find_duplicate2(a):
    n = len(a) - 1
    sum_n = n*(n+1)/2

    return int(sum(a) - sum_n)


# Solution #3: based on Floyd's tortoise and hair cycle-finding algo
# O(n) time, O(1) space
def find_duplicate3(a):
    # 1. find x_i = x_2i
    # Eventually, both tortoise and hare inside cycle, and distance between them
    # (which is same as position of tortoise) is divisible by period lambda of cycle.
    tortoise = a[0]
    hare = a[a[0]]
    while tortoise != hare:
        tortoise = a[tortoise]
        hare = a[a[hare]]

    # 2. Find start of cycle.
    # Reset hare to position 0.  Distance between hare and tortoise still divisible by lambda.
    # Advancing at equal pace, they will be equal when hare hits start of cycle.
    hare = 0
    while tortoise != hare:
        tortoise = a[tortoise]
        hare = a[hare]

    return hare


n = 10
a = list(range(1,n+1))

r = random.randint(1,n)
a.append(r)
random.shuffle(a)

x = find_duplicate(a)
x = find_duplicate2(a)
x = find_duplicate3(a)

print("array = {}".format(a))
print("random int added = {}".format(r))
print("duplicate1 found = {}".format(x))
print("duplicate2 found = {}".format(x))
print("duplicate3 found = {}".format(x))


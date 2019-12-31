"""
dcp#283

This problem was asked by Google.

A regular number in mathematics is defined as one which evenly divides some power of 60. Equivalently, we can say that a regular number is one whose only prime divisors are 2, 3, and 5.

These numbers have had many applications, from helping ancient Babylonians keep time to tuning instruments according to the diatonic scale.

Given an integer N, write a program that returns, in order, the first N regular numbers.
"""


"""
1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30, 32, 36, 40, 
45, 48, 50, 54, 60, 64, 72, 75, 80, 81, 90, 96, 100, ...

NOT:
7, 11, 13, 14, 17, 19, 21, 22, 23, 26, 28, 29, 31, 33, 34, 35, 37, 38, 39, 
41, 42, 43, 44, 46, 47, 55, 56, 57, 58, 59, 61, 62, 63, 65, 66, 67, 68, 69,
70, 71, 73, 74, 76, 77, 78, 79, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92, 93,
94, 95, 97, 98, 99, ...

"""

from timeit import default_timer as timer
import heapq


def is_regular(n):
    while n % 2 == 0:
        n //= 2

    while n % 3 == 0:
        n //= 3

    while n % 5 == 0:
        n //= 5

    return n == 1

"""
Solution #1
Something like O(n log n) due to checking divisibility by 2, 3, and 5
O(n) space due to keeping list of regular numbers, but this isn't essential.
"""
def first_n_regular(n):
    regulars = []
    num_reg = 0
    i = 1 # integers to check if regular or not

    while num_reg < n:
        if is_regular(i):
            num_reg += 1
            regulars.append(i)

        i += 1

    return regulars

"""
Solution#2: use DP: memoization
Faster than solution #1.
O(n log n) due to sorting at end.
O(n) space due to needing to keep track of regular numbers to 
check if i // 2, etc., are in regulars.
"""
def first_n_regular_memo(n):
    regulars = {1} # set
    num_reg = 1
    i = 2 # integers to check if regular or not

    while num_reg < n:
        if ((i % 2 == 0) and (i // 2 in regulars)) \
            or ((i % 3 == 0) and (i // 3 in regulars)) \
            or ((i % 5 == 0) and (i // 5 in regulars)):

            regulars.add(i)
            num_reg += 1

        i += 1

    return sorted(regulars)


"""
Solution #3: use DP: tabulation
But it's difficult to order the numbers.
Use fact that every new regular number comes from a previous regular number,
but multiplied by 2, 3, or 5.  For each of these factors (2, 3, 5), keep track
of the last regular number that it multiplied.

O(n) time
O(n) space

https://cs.stackexchange.com/questions/39689/how-can-i-generate-first-n-elements-of-the-sequence-3i-5j-7k

"""
def first_n_regular_tabulation(n):
    num_reg = 1
    regulars = [1]

    x = y = z = 1 # last regular numbers that 2, 3, or 5 multiplied, respectively
    i = j = k = 0 # indices corresponding to x, y, z
    
    while num_reg < n:
        m = min(2*x, 3*y, 5*z)
        regulars.append(m)
    
        # Note: the 3 possibilities below are not exclusive.
        if m == x*2: 
            i += 1
            x = regulars[i]
        if m == y*3: 
            j += 1
            y = regulars[j]
        if m == z*5: 
            k += 1  
            z = regulars[k]

        num_reg += 1

    return regulars

"""
Solution #4: using priority queue (heap).
Better to use a heap that is also a set.

O(n log n) since insert/remove from heap are O(log n).
[set operations are O(1) amortized avg case, but O(n) actual worst case...]
O(n) space
"""
def first_n_regular_heap(n):
    num_reg = 0
    regulars = []
    
    h = [1] # heap
    pushed_so_far = {1} # set to parallel heap h

    while num_reg < n:
        x = heapq.heappop(h) # O(log (heap size)) <= O(log n)
        regulars.append(x)
        num_reg += 1

        for k in [2, 3, 5]:
            y = x * k
            if y not in pushed_so_far: # O(1) in practice
                heapq.heappush(h, y) # O(log (heap size)) <= O(log n)
                pushed_so_far.add(y) # O(1) amortized avg case...

    return regulars


###############################################################################

# for i in range(1, 101):
#     if is_regular(i):
#         print(i)

n = 200
print("n = {}".format(n))

start = timer()
regulars = first_n_regular(n)
end = timer()
print("\nSolution #1:\n{}".format(regulars))
print("time: {}".format(end - start))

start = timer()
regulars2 = first_n_regular_memo(n)
end = timer()
print("\nSolution #2 (memoization):\n{}".format(regulars2))
print("time: {}".format(end - start))
print("\nAre this solution the same as first one? {}".format(regulars == sorted(regulars2)))

start = timer()
regulars3 = first_n_regular_tabulation(n)
end = timer()
print("\nSolution #3 (tabulation):\n{}".format(regulars3))
print("time: {}".format(end - start))
print("\nAre this solution the same as first one? {}".format(regulars == regulars3))

start = timer()
regulars4 = first_n_regular_heap(n)
end = timer()
print("\nSolution #4 (heap):\n{}".format(regulars4))
print("time: {}".format(end - start))
print("\nAre this solution the same as first one? {}".format(regulars == regulars4))

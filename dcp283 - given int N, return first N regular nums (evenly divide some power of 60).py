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

def is_regular(n):
    while n % 2 == 0:
        n //= 2

    while n % 3 == 0:
        n //= 3

    while n % 5 == 0:
        n //= 5

    return n == 1


# Solution #1
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


# Solution#2: use memoization
# Only seems to be twice as fast as solution#1.
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

    return regulars


# for i in range(1, 101):
#     if is_regular(i):
#         print(i)

n = 500
print("n = {}".format(n))

start = timer()
regulars = first_n_regular(n)
end = timer()
print("\nSolution #1:\n{}".format(regulars))
print("time: {}".format(end - start))

start = timer()
regulars2 = first_n_regular_memo(n)
end = timer()
print("\nSolution #2 (memoization):\n{}".format(regulars))
print("time: {}".format(end - start))

print("\nAre the 2 solutions the same? {}".format(regulars == sorted(regulars2)))


"""
dcp#372

This problem was asked by Amazon.

Write a function that takes a natural number as input and returns the number of digits the input has.

Constraint: don't use any loops.
"""

from math import floor, log10

# Solution using recursion (no loops)
# Assume n is positive integer
def num_digits(n):
    if n == 0:
        return 0

    return num_digits(n//10) + 1

# Math solution
def num_digits2(n):
    return floor(log10(n)) + 1

# Solution: convert to string
def num_digits3(n):
    return len(str(n))

# Using loop
def num_digits4(n):
    d = 0
    while n > 0:
        d += 1
        n //= 10

    return d


n = 1
n = 1234567890
d = num_digits4(n)

print("n = {}".format(n))
print("num digits = {}".format(d))


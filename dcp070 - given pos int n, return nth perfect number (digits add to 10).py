"""
dcp#70

This problem was asked by Microsoft.

A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.
"""

"""
19
28
37
46
55
64
73
82
91
109 *** skipped 100
118
127
136
145
154
163
172
181
190
208 - #20 *** skipped 199
...
271
280 - #28
307 - #29 *** skipped 289, 298
316 - #30
...
370 - #36
406 - #37 *** skipped 379, 388, 397

"""

# Do we do summation of digits recursively? Assume not.

# Must be of form 9x + 1.
# If digits of x add to 10, then digits of x-1 add to 9.
# So x-1 is divisible by 9.  So x = 9k + 1 for some k.

# Converse not true.

################################################################################

def sum_digits(x):
    sum = 0

    while x > 0:
        sum += x % 10
        x //= 10

    return sum


# Assume n is integer >= 1
def perfect_number(n):
    k = 0
    x = 10

    while k < n:
        x += 9

        if sum_digits(x) == 10:
            k += 1

    return x

################################################################################

# Solution #2

# Exceptions to 9k + 1: 100, 199, 289, 298, ...
# Note digits of 199, 289, and 298 don't sum to 10, but recursively they do.

# If we allow recursive sums, then the only integers of form 9k + 1
# that don't have digits recursively summing to 10 are powers of 10.
# Eg, 10, 100, 1000, 10000, ...

# In this case, the function perfect_number(n) can be implemented in
# constant time and constant space.

# If we disallow recursive sums, there still seems to be a pattern....

# Not going to go further into this.

################################################################################

#n = 10
#print("sum_digits({}) = {}".format(n, sum_digits(n)))

for n in range(1, 100):
    print("{}: {}".format(n, perfect_number(n)))




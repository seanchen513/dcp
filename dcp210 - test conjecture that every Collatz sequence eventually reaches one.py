"""
dcp#210

This problem was asked by Apple.

A Collatz sequence in mathematics can be defined as follows. Starting with any positive integer:

if n is even, the next number in the sequence is n / 2
if n is odd, the next number in the sequence is 3n + 1
It is conjectured that every such sequence eventually reaches the number 1. Test this conjecture.

Bonus: What input n <= 1000000 gives the longest sequence?
"""


# Starting with a positive integer n.
# Value of 1000 for num_iterations is good enough for n up to at least 1e9
# Value of 1350 for num_iterations is good enough for n up to at least 1e12
# Value of 1865 for num_iterations is good enough for n up to at least 1e15
# source: https://en.wikipedia.org/wiki/Collatz_conjecture
#
# Optimizations that could be done:
# - Use shortcut formula: a_{n+2} = (3 * a_{n} + 1) / 2 for odd n
# - Use formula to jump ahead k steps, with a time-space tradeoff
# - Memoization
def collatz(n, num_iterations=1000):
    if n == 1:
        return True, 0

    for i in range(1, num_iterations + 1):
        if n % 2: # odd
            n = 3*n + 1
        else: # even
            n /= 2
        
        if int(n) == 1:
            return True, i # index i where n first becomes 1 is called the total stopping time of initial n

    return False, n
    #return int(n)


# Don't bother computing for n such that 2*n <= n_max, that is, n <= n_max / 2
# because there is a power-of-2 multiple of it that is also in interval (n_max/2, n_max]
def max_stopping_time(n_max=1000):
    num_iterations = 10000
    max_stop_time = 0
    n_with_max_stop_time = None

    start = int(n_max / 2)
    for n in range(start, n_max + 1):
        one_reached, stopping_time = collatz(n, num_iterations)

        if not one_reached:
            print("1 was not reached for {} with num_iterations = {}".format(n, num_iterations))
            
            num_iterations *= 2
            print("Extending num_iterations to {} and retrying.".format(num_iterations))

            one_reached, stopping_time = collatz(n, num_iterations)

        #max_stop_time = max(max_stop_time, stopping_time)
        if stopping_time > max_stop_time:
            max_stop_time = stopping_time
            n_with_max_stop_time = n

    return max_stop_time, n_with_max_stop_time


################################################################################

n = 1 # boundary case
n = 2

print("n = {}".format(n))

one_reached, n = collatz(n)
if one_reached:
    print("1 reached at total stopping time = {}".format(n))
else:
    print("1 never reached with final n = {}".format(n))

### values confirmed at: https://en.wikipedia.org/wiki/Collatz_conjecture
#n_max = 100 # max stopping time = 118 for n = 97
#n_max = 1000 # max stopping time = 178 for n = 871
#n_max = 10000 # max stopping time = 261 for n = 6171
#n_max = 100000 # max stopping time = 350 for n = 77031
n_max = 1000000 # max stopping time = 524 for n = 837799

max_stop_time, n_with_max_stop_time = max_stopping_time(n_max)
print("\nFor n up to {}, max stopping time = {} for initial value {}".format(n_max, max_stop_time, n_with_max_stop_time))

# We tested that the Collatz conjecture holds for positive integers n up to 1,000,000
# Note: if max_stopping_time(n_max) returns < n_max, this implies that the stopping times for
# all positive integers <= n_max are also < n_max.  That is, they all reach 1.


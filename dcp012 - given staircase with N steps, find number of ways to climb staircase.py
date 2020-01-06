"""
dcp#12, #413
dip#14
LC70

This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""

"""
Building a recursion tree, where each root to leaf path has same sum.

1
    1
        1 + 1
        2
    2 + 1
2
    1 + 1
    2

"""

"""
{1, 2}:
res[1] = 1
res[2] = 2 (2, 1+1)

res[n] = res[n-1] + res[n-2]
res[3] = res[2] + res[1] = 2 + 1 = 3
res[4] = res[3] + res[2] = 3 + 2 = 5

3: 3, 1+1+1
4: 1+(3), 1+(1+1+1+1), 2+(2), 2+(1+1)
"""


"""
{1, 3, 5}:
res[1] = 1
res[2] = 1
res[3] = 2 (3, 1+1+1)
res[4] = 3 (3+1, 1+3, 1+1+1+1)
res[5] = 5 (5, 3+1+1, 1+3+1, 1+1+3, 1+1+1+1+1)

res[n] = res[n-1] + res[n-3] + res[n-5]
res[6] = res[5] + res[3] + res[1] = 5 + 2 + 1 = 8

1: 1
3: 3, 1+1+1
5: 5, 3+1+1, 1+3+1, 1+1+3, 1+1+1+1+1
6: 1+(5), 1+(3+1+1), 1+(1+3+1), 1+(1+1+3), 1+(1+1+1+1+1),
    3+(3), 3+(1+1+1),
    5+(1)

"""

# Fibonacci sequence: 1, 1, 2, 3, 5, 8, ... for n = 0, 1, 2, 3, ...

# For case of steps = {1, 2}, since it's the Fibonacci sequence,
# can calculate using factorials.  
# O(1) time.
def fib_phi(n):
    phi = (1 + 5**0.5) / 2

    # This formula is based on starting index 1, so shift it
    # (change n to n+1), so that the starting index for our function is 0.
    return int(( phi**(n+1) - (1-phi)**(n+1) ) / (5**0.5))


# Solution: iterative, only for steps = {1, 2}
# O(n) time, O(1) space
def fib(n):
    a, b = 1, 1

    for _ in range(n):
        a, b = b, a + b

    return a


###############################################################################

# Solution#1: recursion
# Generalizes Fibonacci sequence.
# Fibonacci sequence is given when steps = {1, 2}.
# Time complexity: exponential...  O(|steps|^n)
def num_ways_climb(n, steps={1, 2}):
    if n < 0:
        return 0

    if n == 0:
        return 1
   
    #return num_ways_climb(n-1) + num_ways_climb(n-2)
    return sum(num_ways_climb(n - i, steps) for i in steps)


# Solution#2: DP using memoization (but otherwise like solution#1)
# O(n*|steps|)
# O(n) space
def num_ways_climb_memo(n, steps={1, 2}, store={}):
    if n < 0:
        return 0

    if n == 0:
        return 1
   
    if n not in store:
        store[n] = sum(num_ways_climb_memo(n - i, steps) for i in steps)
    
    return store[n]


# Solution#3: DP using tabulation
# O(n*|steps|) time
# O(n) space
def num_ways_climb_tab(n, steps={1, 2}):
    res = [0]*(n+1)

    res[0] = 1
    if (1 in steps) and (n >= 1):
        res[1] = 1

    for total_steps in range(2, n+1):
        # for step in steps:
        #     if step <= total_steps:
        #         res[total_steps] += res[total_steps - step]
        res[total_steps] = sum(res[total_steps - step] for step in steps if step <= total_steps)

    return res[n]


###############################################################################


n = 20
steps = {1}
steps = {5}
steps = {2, 3}
steps = {4, 6}
steps = {3, 5}
#steps = {1, 3, 5}
#steps = {1, 5}
steps = {1, 2}

f_phi = fib_phi(n)
f = fib(n)
k = num_ways_climb(n, steps)
k2 = num_ways_climb_memo(n, steps)
k3 = num_ways_climb_tab(n, steps)

print("\nn = {}".format(n))
print("\nsteps = {}".format(steps))

print("\nf_phi = {}".format(f_phi))
print("\nfib = {}".format(f))
print("\nnumber of ways to climb (plain recursion) = {}".format(k))
print("\nnumber of ways to climb (memoization) = {}".format(k2))
print("\nnumber of ways to climb (tabulation) = {}".format(k3))


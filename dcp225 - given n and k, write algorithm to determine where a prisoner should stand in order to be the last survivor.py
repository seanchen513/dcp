"""
dcp#225

This problem was asked by Bloomberg.

There are N prisoners standing in a circle, waiting to be executed. The executions are carried out starting with the kth person, and removing every successive kth person going clockwise until there is no one left.

Given N and k, write an algorithm to determine where a prisoner should stand in order to be the last survivor.

For example, if N = 5 and k = 2, the order of executions would be [2, 4, 1, 5, 3], so you should return 3.

Bonus: Find an O(log N) solution if k = 2.
"""

# Clarify: when counting to execute the kth person in a round, do we skip previously executed people?
# From the given example, the answer seems to be yes.

# Following statements are true is only if we don't skip previously executed people:
# Every prisoner is executed if and only if gcd(n, k) = 1, ie, n and k are relatively prime.
# Cycle length is n/gcd(n,k).
# Last prisoner executed is last one in cycle.

################################################################################
# Naive solution using list
# At least O(n) time; O(nk) ?
# O(n) space
def last_prisoner(n, k):
    exec_order = [0]*n # value is 0 if still alive

    index = -1 # 0-based
    for i in range(1, n + 1): # ith execution

        # find index of next kth prisoner that is still alive
        count = 0
        while count < k:
            index = (index + 1) % n
            if exec_order[index] == 0: # still alive
                count += 1

        exec_order[index] = i
        print("index + 1 = {}".format(index + 1))

    return index + 1, exec_order

################################################################################
# Solution #2: recursion
# O(n) time
def josephus(n, k):
    if n == 1:
        return 1
    else:
        return (josephus(n - 1, k) + k - 1) % n + 1


################################################################################
# Solution #3 (k=2 only):
# O(log n) time for k=2
#
# 1st round: all even-numbered prisoners executed.
#   - if n is odd, execute 1st prisoner at end of round also.
# 2nd round: if n even, f(n) = 2f(n/2) - 1
#   - if n odd, f(n) = 2f((n-1)/2) + 1
# where f(n) = positions of survivors.
# Solution to recurrence relation is increasing odd sequence
# that restart with f(n)=1 whenever n is power of 2.
# Theorem: if n = 2^x + y where 0 <= y < 2^x, then f(n) = 2y + 1.
# Explicitly, y = n - 2^floor(log2(n)), so f(n) = 2[n - 2^floor(log2(n))] + 1.
def josephus2(n):

    # Find power p of 2 that is just above n.
    # Then f(n) = 2n - p + 1 from explicit solution.
    p = 1
    while p <= n:
        p *= 2

    return 2*n - p + 1


# Solution #4 (k=2 only): use bit manipulation
# ....


"""
            exec
1 2 3 4 5       2
1 3 4 5         4
1 3 5           1
3 5             5
3


1   0001
2   0010
3   0011
4   0100
5   0101

"""

def last_prisoner2(n):
    pass


################################################################################


n = 5
k = 1 # 5, order = 1, 2, 3, 4, 5
k = 3 # 4, order = 3, 1, 5, 2, 4 
k = 2 # 3, order = 2, 4, 1, 5, 3

print("\nn = {}, k = {}".format(n, k))

last, exec_order = last_prisoner(n, k)
print("\nSol #1: n = {}, k = {}".format(n, k))
print("last prisoner executed = {}".format(last))
print("execution order for each prisoner = {}".format(exec_order))

last = josephus(n, k)
print("\nSol #2: n = {}, k = {}".format(n, k))
print("last prisoner executed = {}".format(last))

last = josephus2(n)
print("\nSol #3: n = {}, k = 2".format(n))
print("last prisoner executed = {}".format(last))


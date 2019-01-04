"""
dcp#60

This problem was asked by Facebook.

Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it up into two subsets that add up to the same sum.
"""

# multiset = like a set but allows mutilplicities of elements

"""
Note: for n bits, there are 2^n values 0 ... (2^n - 1)
~x = all bits of x flipped
x + ~x = 111..1 = 2^n - 1
Integers that are (2^n - 1) complements (add up to 2^n - 1) have flipped bits.

Example:
0: 000      7: 111
1: 001      6: 110
2: 010      5: 101
3: 011      4: 100
"""

"""
Idea: use bits to represent subsets of given set.
Complementary integers represent partitions of the given set.
If given set has n elements, then we use n bits.
Complementary integers add up to 2^n - 1.
Only necessary to loop from 0 to 2^(n-1) - 1.
"""

def partitions(s):
    # can be partitioned only if sum is even
    if sum(s) % 2 != 0:
        return None

    n = len(s)
    p = 2**n

    for k in range(0, 2**(n-1)):
        sum1 = 0
        sum2 = 0
        s1 = []
        s2 = []

        for b in range(0, n):
            if k & (1 << b):
                sum1 += s[b]
                s1.append(s[b])
            else:
                sum2 += s[b]
                s2.append(s[b])
        
        if sum1 == sum2:
            #return True
            return [sum1, s1, s2]

    return None


s = [15, 5, 20, 10, 35, 15, 10] # can be partitioned
#s = [15, 5, 20, 10, 35] # cannot be partitioned

print("s = {}".format(s))
print("sum(s) = {}".format(sum(s)))

f = partitions(s)

if f is None:
    print("Cannot be partitioned into 2 subsets with same sum.")
else:
    print("Can be partitioned into 2 subsets with same sum.")
    print("Partitions, each with sum {}: {} and {}".format(f[0], f[1], f[2]))



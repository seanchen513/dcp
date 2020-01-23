"""
dcp037

This problem was asked by Google.

The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
"""

"""
LC78. Subsets
Medium

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.
"""

"""
Solution #1: use bit manipulation.

If given set has n elts, its power set has 2**n subsets of it.
Look at bit patterns of all numbers from 0 to 2**n - 1.  
There is a 1-1 correspondence b/w these numbers and subset elts in the power set.
There is a 1-1 correspondence b/w the bits in these numbers and the elements of
the given set.  
If the bit is set, include the element in the subset elt of the power set.

O(2**n) time
O(2**n) extra space

Note: could use frozensets instead (immutable and hashable)
"""

def power_set(s):
    n = len(s)
    
    # p = set() # cannot add sets/lists inside set; get TypeError: unhashable type: 'set'/'list'
    # so use list instead
    pset = [[]] # the empty set is always in the power set

    for k in range(1, 2**n): # kth element of power set
        p_elt = [] # element of power set; subset of given set s

        # for b in range(0, n): # bits in k, or bth element of set s    
        #     if k & (1 << b):
        #         p_elt.append(s[b])

        j = 0
        while k > 0:
            if k & 1:
                p_elt.append(s[j])

            k >>= 1
            j += 1

        # pset.add(p_elt) # cannot add sets/lists inside set; get TypeError: unhashable type: 'set'/'list'
        pset.append(p_elt)

    return pset

"""
Solution #2
"""
import itertools

def power_set2(s):
    n = len(s)
    pset = [[]]

    for k in range(1, n+1):
        pset.extend([list(p) for p in itertools.combinations(s, k)])
        
    return pset

"""
Solution #3
"""
def power_set3(s):
    return list(itertools.chain.from_iterable(
        [list(p) for p in itertools.combinations(s, k)] for k in range(0, len(s)+1)
    ))

###############################################################################

if __name__ == "__main__":
    # using list to represent set
    s = []
    s = [1]
    s = ['a', 'b', 'c']
    s = [1, 2, 3] 

    p = power_set(s)
    p2 = power_set2(s)
    p3 = power_set3(s)

    print("\nset = {}".format(s))
    print("\npower set (sol #1) = {}".format(p))
    print("\npower set (sol #2) = {}".format(p2))
    print("\npower set (sol #3) = {}".format(p3))

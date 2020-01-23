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

O(n * 2^n) time
O(2^n) extra space

Note: could use frozensets instead (immutable and hashable)
Output is NOT sorted by size.
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
Solution #1b: same idea as sol #1, but expressed differently.  Slower?
"""
def power_set1b(s):
    n = len(s)
    
    pset = [[]] # the empty set is always in the power set

    for k in range(1, 2**n): # kth element of power set
        pset.append([s[j] for j in range(n) if (k >> j) & 1])
    
    return pset

###############################################################################

"""
Solution #2: use Python's itertools.combinations()

Output is sorted by size, and then sorted lexicographically.
"""
import itertools

def power_set2(s):
    n = len(s)
    pset = [[]]

    for k in range(1, n+1):
        pset.extend([list(p) for p in itertools.combinations(s, k)])
        
    return pset

"""
Solution #2b: like sol #2, but also use itertools.chain.from_iterable()
along with itertools.combinations()
"""
def power_set2b(s):
    return list(itertools.chain.from_iterable(
        [list(p) for p in itertools.combinations(s, k)] for k in range(0, len(s)+1)
    ))

###############################################################################
"""
Solution #3: Recursion on number of elements in given set.
For each element in set, we can pick it to include in a new subset or not.

O(n * 2^n) time
O(2^n) extra space

Output is NOT sorted by size.
"""
def power_set3(s):
    if not s:
        return [[]]

    pset = power_set3(s[:-1])

    return pset + [set1 + [s[-1]] for set1 in pset]


"""
Solution #3b: Iterative version of sol #3.

O(n * 2^n) time
O(2^n) extra space
"""
def power_set3b(s):
    pset = [[]]

    for elt in s:
        #pset.append(set1 + [elt] for set1 in pset) # doesn't work
        pset += [set1 + [elt] for set1 in pset]

    return pset

###############################################################################

"""
Solution #4: Backtracking

O(n * 2^n) time
O(2^n) extra space

Output is sorted by size, and then sorted lexicographically.
"""
def power_set4(s):
    def backtrack(first=0, curr=[]):
        # check if the combination is done
        if len(curr) == k:
            pset.append(curr[:])
            return

        for i in range(first, n):
            # add element to current combo
            curr.append(s[i])

            # recurse to check again and add more elements
            backtrack(i+1, curr)

            # backtrack
            curr.pop()

    pset = []
    n = len(s)

    for k in range(n+1): # length of combo
        backtrack()

    return pset

###############################################################################

if __name__ == "__main__":
    # using list to represent set
    s = []
    s = [1]
    s = ['a', 'b', 'c']
    s = [1, 2, 3] 

    p = power_set(s)
    p1b = power_set1b(s)
    p2 = power_set2(s)
    p2b = power_set2b(s)
    p3 = power_set3(s)
    p3b = power_set3b(s)
    p4 = power_set4(s)

    print("\nset = {}".format(s))
    print("\npower set (sol #1)  = {}".format(p))
    print("\npower set (sol #1b) = {}".format(p1b))
    print("\npower set (sol #2)  = {}".format(p2))
    print("\npower set (sol #2b) = {}".format(p2b))
    print("\npower set (sol #3)  = {}".format(p3))
    print("\npower set (sol #3b) = {}".format(p3b))
    print("\npower set (sol #4)  = {}".format(p4))

"""
dcp#37

This problem was asked by Google.

The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
"""


# form intgers with n bits
# loop from 0 to 2^n - 1
# each integer represent an element of the power set
# each bit in the integer represent whether each element in s is in the power set element

# note: could use frozensets instead (immutable and hashable)

def power_set(s):
    n = len(s)
    
    # p = set() # cannot add sets/lists inside set; get TypeError: unhashable type: 'set'/'list'
    p = []
    for k in range(0, 2**n): # kth element of power set
        p_elt = []

        for b in range(0, n): # bits in k, or bth element of set s    
            if k & (1 << b):
                p_elt.append(s[b])

        # p.add(p_elt) # cannot add sets/lists inside set; get TypeError: unhashable type: 'set'/'list'
        p.append(p_elt)

    return p


# using list to represent set
s = []
s = [1]
s = ['a', 'b', 'c']
s = [1, 2, 3] 

p = power_set(s)

print("set = {}".format(s))
print("power set = {}".format(p))


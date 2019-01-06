"""
dcp#96

This problem was asked by Microsoft.

Given a number in the form of a list of digits, return all possible permutations.

For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].
"""

import pprint

# Build recursion tree.
# Each new child node is based on new array with kth element 
# swapped with one of the elements to its right.
def all_perms(a, n, k, p):
    # only add permutation to list p at bottom level of recursion tree
    if k == n - 1:
        p.append(a)
        return

    for i in range(k, n):        
        b = a[:]

        if i > k:
            temp = b[k]
            b[k] = b[i]
            b[i] = temp

        all_perms(b, n, k+1, p)


a = [1, 2, 3]
a = [1, 2, 3, 4]

n = len(a)
print("a = {}".format(a))

p = []
all_perms(a, n, 0, p)
print("\nall permutations:")
pprint.pprint(p)

print("\nall permutations, sorted:")
p.sort()
pprint.pprint(p)

num_p = len(p)
print("\nCheck number of elemeents in p: {}".format(num_p))


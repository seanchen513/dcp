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
def all_perms(arr, k, perms):
    # only add permutation to list "perms" at bottom level of recursion tree
    if k == len(arr) - 1:
        perms.append(arr)
        return

    for i in range(k, len(arr)):        
        b = arr[:]
        b[i], b[k] = b[k], b[i] # swap

        all_perms(b, k+1, perms)


a = [1, 2, 3]
a = [1, 2, 3, 4]

print("a = {}".format(a))

perms = []
all_perms(a, 0, perms)
print("\nall permutations:")
pprint.pprint(perms)

print("\nall permutations, sorted:")
perms.sort()
pprint.pprint(perms)

num_perms = len(perms)
print("\nCheck number of elemeents in p: {}".format(num_perms))


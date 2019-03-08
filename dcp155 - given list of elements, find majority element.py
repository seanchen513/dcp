"""
dcp#155

This problem was asked by MongoDB.

Given a list of elements, find the majority element, which appears more than half the time (> floor(len(lst) / 2.0)).

You can assume that such element exists.

For example, given [1, 2, 1, 1, 3, 4, 0], return 1. [sic: bad example]
"""

# As stated in problem statement, we assume that a majority element exists.

import math

# Solution #1 basic
# O(n^2) time, O(1) space
def find_majority_elt(a):
    for x in a:
        count = 0
        for y in a:
            if x == y:
                count += 1
            
            if count > len(a) // 2:
            #if count > math.floor(len(a) / 2):
                return y


# Solution #2 using binary search tree
# O(n^2) time for regular BST; O(n log n) for self-balancing BST
# O(n) space
def find_majority_elt2(a):
    b = bst() # NOT IMPLEMENTED HERE

    for x in a:
        node = b.find(X)

        if node is None:
            b.insert(x)
        
        else:
            node.count += 1
            if node.count > len(a) // 2:
                return node.val
                

# Solution #3 using Boyer-Moore maority vote algorithm
# O(n) time, O(1) space
#
# No need to validate that element found by algo is indeed a majority element
# due to assumption of problem statement.
def find_majority_elt3(a):
    maj_index = 0
    count = 1

    for i in range(0, len(a)):
        if a[i] == a[maj_index]:
            count += 1
        else:
            count -= 1
        
        if count == 0:
            maj_index = i
            count = 1

    return a[maj_index]


# Solution #4 using hashmap (Python dict)
# O(n) time, O(n) space
def find_majority_elt4(a):
    d = {}
    for x in a:
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1

    return max(d, key=lambda k: d[k])


a = [1, 2, 1, 1, 3, 4, 1] # modified example from problem statement

x = find_majority_elt(a)
print("method 1: majority element = {}".format(x))

#x = find_majority_elt2(a)
#print("method 2: majority element = {}".format(x))

x = find_majority_elt3(a)
print("method 3: majority element = {}".format(x))

x = find_majority_elt4(a)
print("method 4: majority element = {}".format(x))


"""
dcp#179

This problem was asked by Google.

Given the sequence of keys visited by a postorder traversal of a binary search tree, reconstruct the tree.

For example, given the sequence 2, 4, 3, 8, 7, 5, you should construct the following tree:

    5
   / \
  3   7
 / \   \
2   4   8
"""

# Clarify: can we assume that tree is complete?  That is, every level is filled except
# for possibly last one, which is filled from left to right.
# Probably not, since the given example is a bit off from being complete.

# Clarify: can we assume no duplicate keys?  Assume yes.

# Assume given sequence is valid post-order traversal of a BST.


class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_tree(root, depth=0):
    if root is None:
        return

    print_tree(root.right, depth + 1)
    print("  "*depth + str(root.val))
    print_tree(root.left, depth + 1)


# Solution #1: In post-order traversal, last element is root.
# The 1st part of the rest of array is left subtree, and the 2nd part is right subtree.
# Problem is to find the boundary between the left and right subtrees.
# O(n^2) time; O(n log n) if use binary search.
# O(n) space for recursion call stack.
#
# Improvements: binary search; pass start and end of subarrays rather than slices.
def reconstruct_bst(seq):
    if (seq is None) or (len(seq) == 0):
        return None

    root = Node(seq[-1])
    
    # Could write binary search function.
    # right_first = first index in seq where right subtree values start.
    right_first = 0
    while right_first in range(0, len(seq) - 1):
        if seq[right_first] < root.val:
            right_first += 1
        else:
            break

    root.left = reconstruct_bst(seq[:right_first])
    root.right = reconstruct_bst(seq[right_first:-1])

    return root

################################################################################
# Solution #2: same as solution #1 but passes array start and end rather than slices.
# Also uses binary search.
# O(n log n) time
# O(n) space for recursion call stack
def reconstruct_bst2(seq, left, right):
    if left > right:
        return None

    root = Node(seq[right])
    
    left_last = find_last_smaller(seq, left, right - 1, root.val) 

    root.left = reconstruct_bst2(seq, left, left_last)
    root.right = reconstruct_bst2(seq, left_last + 1, right - 1)

    return root


# Binary search utility function for reconstruct_bst2().
# Finds last index in seq that is between left and right indices such that seq[index] < val.
# Assumes first part of seq between left and right indices are < val,
# and second part of seq is > val.
def find_last_smaller(seq, left, right, val):
    if (left > right) or (seq[left] > val):
        return left - 1

    low = left
    high = right

    while (low < high) and (seq[high] > val):    
        mid = low + (high - low + 1) // 2
        if seq[mid] > val:
            high = mid - 1
        else:
            low = mid

    return high

################################################################################
# Solution #3: iterative solution using stack.
# Use Python list with append() and pop() as a stack.
# O(n log n) time
# O(n) space due to stack.
def reconstruct_bst3(seq):
    if (seq is None) or (seq == []):
        return None

    root = Node(seq[-1])
    stack = [root]
    index = len(seq) - 2

    while index >= 0:
        node = Node(seq[index])

        # Keep popping nodes while top of stack is greater.
        temp = None
        while (len(stack) > 0) and (stack[-1].val > seq[index]):
            temp = stack.pop()

        if temp is not None:
            temp.left = node
        else:
            stack[-1].right = node

        stack.append(node)
        index -= 1

    return root

"""
[2, 4, 3, 8, 7, 5]
 0  1  2  3  4  5 = index

stack       index       seq[index]      popped:
========================================================================
5           4           7               nothing             5.right = 7
5 7         3           8               nothing             7.right = 8
5 7 8       2           3               8 7 5               5.left = 3
3           1           4               nothing             3.right = 4
3 4         0           2               4 3                 3.left = 2

"""

################################################################################
# Solution #4: Read postorder traversal string in reverse...
# O(n) time

INT_MIN = -2**31
INT_MAX = 2**31

# Treat index as a list in order to pass by reference.
def reconstruct_bst4(seq, index=[], min=INT_MIN, max=INT_MAX):
    if (seq is None) or (seq == []) or (seq[0] < 0):
        return None

    if index == []:
       index = [len(seq)-1]
    
    key = seq[index[0]]
    root = None

    if (key > min) and (key < max):
        root = Node(key)
        index[0] -= 1

        if index[0] >= 0:
            # right needs to come before left
            root.right = reconstruct_bst4(seq, index, key, max)
            root.left = reconstruct_bst4(seq, index, min, key)
            
    return root


################################################################################

"""
seq = [1, 2, 3]
  3
 2
1

seq = [1, 3, 2]
 2
1 3

seq = [2, 1, 3]
 3
1
 2

seq = [2, 3, 1]
1
 3
2

seq = [3, 1, 2] # gives tree, but not BST -- sequence does not correspond to a post-order traversal of a BST
Solution #1 and #2 print tree:
2
 1
  3

Solution#4 prints tree:
 2
1

seq = [3, 2, 1]
1
 2
  3
"""

def test_seq(seq):
    print("sequence: {}\n".format(seq))

    #tree = reconstruct_bst(seq)
    #tree = reconstruct_bst2(seq, 0, len(seq) - 1)
    tree = reconstruct_bst3(seq)
    #tree = reconstruct_bst4(seq)

    print_tree(tree)
    print()


tests = [
    [],
    [1],
    [1, 2],
    [2, 1],
    [1, 2, 3],
    [1, 3, 2],
    [2, 1, 3],
    [2, 3, 1],
    [3, 1, 2], # not a valid postorder traversal of a BST
    [3, 2, 1],
    [2, 4, 3, 8, 7, 5], # given example
]

for seq in tests:
    test_seq(seq)




"""
For given example:

[2, 4, 3, 8, 7, 5]
root = 5
left = 2, 4, 3
right = 8, 7

[2, 4, 3]
root = 3
left = 2
right = 4

...

[8, 7]
root = 7
left = None
right = 8

[8]
root = 8
left = None
right = None
"""


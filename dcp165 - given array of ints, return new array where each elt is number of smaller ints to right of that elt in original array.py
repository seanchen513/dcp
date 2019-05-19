"""
dcp#165

This problem was asked by Google.

Given an array of integers, return a new array where each element in the new array is the number of smaller elements to the right of that element in the original input array.

For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:

There is 1 smaller element to the right of 3
There is 1 smaller element to the right of 4
There are 2 smaller elements to the right of 9
There is 1 smaller element to the right of 6
There are no smaller elements to the right of 1
"""

# Clarify: Can there be duplicate elements in given array?

################################################################################
# Solution #1: brute force
# O(n^2) time
def num_smaller_elts(arr):
    result = []

    for i in range(0, len(arr)):
        sum = 0

        for j in range(i, len(arr)):
            if arr[j] < arr[i]:
                sum += 1

        result.append(sum)

    return result

################################################################################
# Solution #2: Use self-balancing BST where each node contains size of its subtree.
# Traverse given array from right to left, inserting elements in tree.  Before inserting,
# compare element to root of tree.  If greater, than # smaller elts is same as size of
# left subtree.  Recursively do this down the tree until element can be added.
# O(n log n) time
def num_smaller_elts2(arr):
    num_smaller = []
    
    root = None

    for k in range(len(arr)-1, -1, -1):
        n_smaller = [0] # list used to hold single number in order to pass by reference
        root = insert(root, arr[k], n_smaller)
        num_smaller.append(n_smaller[0])
    
    return num_smaller[::-1]


class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.size = 1 # size of the subtree rooted at this node
        self.height = 1

def height(root):
    if root is None:
        return 0
    
    return root.height

def size(root):
    if root is None:
        return 0
    
    return root.size

def balance(root):
    if root is None:
        return 0
    
    return height(root.left) - height(root.right)

def update_height(root):
    if root is None:
        return
        
    root.height = max( height(root.left), height(root.right) ) + 1

def update_size(root):
    if root is None:
        return

    root.size = size(root.left) + size(root.right) + 1

def left_rotate(root):
    y = root.right  # R
    t2 = y.left     # RL

    root.right = t2
    y.left = root

    # update heights
    update_height(root)
    update_height(y)

    # update sizes
    update_size(root)
    update_size(y)

    return y # new root

def right_rotate(root):
    y = root.left   # L
    t2 = y.right    # LR

    root.left= t2
    y.right = root

    # update heights
    update_height(root)
    update_height(y)

    # update sizes
    update_size(root)
    update_size(y)

    return y # new root

def insert(root, key, n_smaller):
    if root is None:
        return Node(key)

    if key < root.val:
        root.left = insert(root.left, key, n_smaller)
    else:
        root.right = insert(root.right, key, n_smaller)
        # update count of smaller elements
        n_smaller[0] += size(root.left) + 1

    # Update height and size of ancestor node
    update_height(root)
    update_size(root)

    # If node is unbalanced (|balance| >= 2), there are 4 cases
    bal = balance(root)

    # left-left case
    if (bal > 1) and (key < root.left.val):
        return right_rotate(root)

    # left-right case
    if (bal > 1) and (key > root.left.val):
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # right-right case
    if (bal < -1) and (key > root.right.val):
        return left_rotate(root)

    # right-left case`
    if (bal < -1) and (key < root.right.val):
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


################################################################################

arr = [1]
arr = [1, 2, 3, 4, 5]
arr = [3, 4, 9, 6, 1]

print("array = {}".format(arr))

print("\n# smaller elts to right of each elt:")

arr1 = num_smaller_elts(arr)
print("\nSolution #1 (brute force): {}".format(arr1))

arr2 = num_smaller_elts2(arr)
print("\nSolution #2 (using AVL tree): {}".format(arr2))


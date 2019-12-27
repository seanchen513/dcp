"""
dcp#327

This problem was asked by Salesforce.

Write a program to merge two binary trees. Each node in the new tree should hold a value equal to the sum of the values of the corresponding nodes of the input trees.

If only one input tree has a node in a given position, the corresponding node in the new tree should match that input node.

"""

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


"""
Creates a new binary tree, where each node's value is the sum
of values of the corresponding nodes in the given binary trees.

O(n) time, where n = total number of nodes in both given trees.
"""
def sum_trees(root1, root2):
    if (root1 is None) and (root2 is None):
        return None

    if root2 is None:
        root = Node(root1.val)
        root.left = sum_trees(root1.left, None)
        root.right = sum_trees(root1.right, None)       

    elif root1 is None:
        root = Node(root2.val)
        root.left = sum_trees(None, root2.left)
        root.right = sum_trees(None, root2.right)
    
    else:
        root = Node(root1.val + root2.val)
        root.left = sum_trees(root1.left, root2.left)
        root.right = sum_trees(root1.right, root2.right)

    return root


"""
Merges (via summing) values of root2 into corresponding values of root1.
This modifies root1, but not root2.

However, the merged tree may share nodes with root2, so this is useful only 
if we don't care about preserving use of root2 separately.
"""
def merge_trees(root1, root2):
    if root1 is None:
        return root2
    
    if root2 is None:
        return root1

    root1.val += root2.val

    root1.left = merge_trees(root1.left, root2.left)
    root1.right = merge_trees(root1.right, root2.right)

    return root1


###############################################################################

""" 
from dcp135

  10
 /  \
5    5
 \     \
   2    1
       /
     -1
"""
root2 = Node(10)
l = root2.left = Node(5)
lr = l.right = Node(2)
r = root2.right = Node(5)
rr = r.right = Node(1)
rrl = rr.left = Node(-1)

"""
from dcp394

    8
   / \
  4   13
 / \   \
2   6   19
"""
root1 = Node(8)
root1.left = Node(4)
root1.left.left = Node(2)
root1.left.right = Node(6)
root1.right = Node(13)
root1.right.right = Node(19)

"""
      1
     /
    2
   /
  3
 /
4
"""
root3 = Node(1)
root3.left = Node(2)
root3.left.left = Node(3)
root3.left.left.left = Node(4)

"""
5
 \
  6
   \
    7
     \
      8
"""
root4 = Node(5)
root4.right = Node(6)
root4.right.right = Node(7)
root4.right.right.right = Node(8)

###############################################################################

def test(root1, root2, test_type='sum'):
    print("\n### Test type: {}".format(test_type))

    print("\nFirst tree:")
    print_tree(root1)

    print("\nSecond tree:")
    print_tree(root2)

    if test_type == 'sum':
        print("\nSum of trees:")
        summed = sum_trees(root1, root2)
        print_tree(summed)

        print("\n### Modifying node value in 2nd tree...")
        root2.right.val = -999

        print("\nFirst tree:")
        print_tree(root1)

        print("\nSecond tree:")
        print_tree(root2)

        print("\nPreviously summed tree:")
        print_tree(summed)

    elif test_type == 'merge':
        print("\nMerged trees:")
        merged = merge_trees(root1, root2)
        print_tree(merged)
        
        print("\n### Modifying node value in 2nd tree...")
        root2.right.val = -999

        print("\nFirst tree:")
        print_tree(root1)

        print("\nSecond tree:")
        print_tree(root2)

        print("\nPreviously merged tree:")
        print_tree(merged)


test_type = 'sum'
#test_type = 'merge'

#test(None, None, test_type)
#test(root1, None, test_type)
#test(None, root2, test_type)

#test(root1, root2, test_type)
#test(root2, root1, test_type)
#test(root1, root1, test_type)
#test(root2, root2, test_type)

test(root3, root4, test_type)
#test(root4, root3, test_type)
#test(root3, root3, test_type)
#test(root4, root4, test_type)

#test(root1, root3, test_type)
#test(root1, root4, test_type)
#test(root2, root3, test_type)
#test(root2, root4, test_type)


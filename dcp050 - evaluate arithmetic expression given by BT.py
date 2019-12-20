"""
dcp#50

This problem was asked by Microsoft.

Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5).
"""


class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Use post-order evaluation since a node that is an operator
# may have operators as children.
def evaluate_bt(root):
    # if root is None:
    #     return

    if type(root.val) in {int, float}:
        return root.val

    l = evaluate_bt(root.left)
    r = evaluate_bt(root.right)

    if root.val == '+':
        return l + r
    if root.val == '-':
        return l - r
    if root.val == '*':
        return l * r
    if root.val == '/':
        return l / r

    # return root.val


root = Node('*')
root.left = Node('+')
root.left.left = Node(3)
root.left.right = Node(2)

root.right = Node('+')
root.right.left = Node(4)
root.right.right = Node(5)

answer = evaluate_bt(root)

print("answer = {}".format(answer))



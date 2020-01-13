"""
dcp#116

This problem was asked by Jane Street.

Generate a finite, but an arbitrarily large binary tree quickly in O(1).

That is, generate() should return a tree whose size is unbounded but finite.
"""

# https://dailycodingproblem.com/blog/big-tree/

import random

class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left= left
        self.right = right


def print_tree(root, depth=0):
    if root is None:
        return
    
    print_tree(root.right, depth + 1)
    print("  "*depth + str(root.val))
    print_tree(root.left, depth + 1)


# Eager tree generation - ignore O(1) generation constraint
# Generates left and right subtrees recursively x% of the time (50% here)
def generate():
    root = Node(0)

    if random.random() < 0.5:
        root.left = generate()
    
    if random.random() < 0.5:
        root.right = generate()

    return root


################################################################################
# Lazy tree generation
# Use Python's "property" keyword, which lets us define a property on an object at look-up.
# When the "left" or "right" property is looked up, we check if that subtree has been evaluated.
# If not, we recursively create a new node half the time.  If it has been evaluated, we just
# return that node.
# O(1) time
# Note 5/10/19: this doesn't seem to work in Python 3.7.1.
def generate_lazy():
    return Node2(0)

class Node2():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self._left= left
        self._right = right

        self._is_left_evaluated = False
        self._is_right_evaluated = False

        @property
        def _left(self):
            if not self._is_left_evaluated:
                if random.random() < 0.5:
                    self._left = Node2(0)

            self._is_left_evaluated = True
            return self._left

        @property
        def _right(self):
            if not self._is_right_evaluated:
                if random.random() < 0.5:
                    self._right = Node2(0)

            self._is_right_evaluated = True
            return self._right

    #     self.test()

    # def test(self):
    #     self._left
    #     print(self._left)


def print_tree2(root, depth=0):
    if root is None:
        return
    
    print_tree(root._right, depth + 1)
    print("  "*depth + str(root.val))
    print_tree(root._left, depth + 1)

################################################################################

root = generate()
print_tree(root)

# 5/10/19: doesn't work
# root = generate_lazy()
# print_tree2(root)


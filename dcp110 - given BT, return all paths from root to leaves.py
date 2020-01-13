"""
This problem was asked by Facebook.

Given a binary tree, return all paths from the root to leaves.

For example, given the tree

   1
  / \
 2   3
    / \
   4   5
it should return [[1, 2], [1, 3, 4], [1, 3, 5]].
"""


class Node():
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def all_paths_util(root, rec_stack, paths):
    rec_stack.append(root.val)

    if (root.left is None) and (root.right is None):
        paths.append(rec_stack[:])
        rec_stack.pop()
        return

    if root.left is not None:
        all_paths_util(root.left, rec_stack, paths)

    if root.right is not None:
        all_paths_util(root.right, rec_stack, paths)

    rec_stack.pop()


def all_paths(root):
    if root is None:
        return []

    paths = []
    rec_stack = []

    all_paths_util(root, rec_stack, paths)

    return paths


root = None
root = Node(1)

root = Node(1, 
        Node(2), 
        Node(3, 
            Node(4), 
            Node(5)
            )
        )

root = Node(1, Node(2, Node(3, Node(4, Node(5)))))

root = Node(1, 
        Node(2, 
            Node(4), 
            Node(5)
            ),
        Node(3, 
            Node(6), 
            Node(7)
            )
        )

paths = all_paths(root)

print(paths)


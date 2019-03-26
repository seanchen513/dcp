"""
dcp#107

This problem was asked by Microsoft.

Print the nodes in a binary tree level-wise. For example, the following should print 1, 2, 3, 4, 5.

  1
 / \
2   3
   / \
  4   5

"""

# Ask if ok to print different levels on different lines.


class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution #1: use a list for each level
# Can print one level per line easily.
def print_levelwise(root):
    current_level = [root]

    while current_level:
        print(' '.join(str(x.val) for x in current_level))

        next_level = []
        for x in current_level:
            if x.left is not None:
                next_level.append(x.left)
            if x.right is not None:
                next_level.append(x.right)

        current_level = next_level


from collections import deque

# Solution #2: use deque as queue
def print_levelwise2(root):
    q = deque()
    q.append(root)

    while q:
        node = q.popleft()
        print(str(node.val), end=' ')

        if node.left is not None:
            q.append(node.left)

        if node.right is not None:
            q.append(node.right)

    print()


root = Node(1)
root.left = Node(2)
root.right = Node(3, Node(4), Node(5))


print_levelwise(root)
"""
prints:
1
2 3
4 5
"""

print()
print_levelwise2(root)
# prints: 1 2 3 4 5 


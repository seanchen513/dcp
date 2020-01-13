"""
dcp#117

This problem was asked by Facebook.

Given a binary tree, return the level of the tree with minimum sum.
"""


class Node:
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


# Let root be at level 0.
# Do level-order traversal of tree using a queue.
# For queue, use built-in list with append() and pop(0).
# For queue, could also use collections.deque with append() and popleft().
# O(n) time since traverse entire tree.
# O(n) space because of queue.
def level_with_min_sum(root):
    if root is None:
        return None, None
    
    min_sum = root.val
    min_level = 0
    level = 0
    q = [root]

    while len(q) > 0:
        count = len(q)
        sum = 0

        while count > 0: # current level
            node = q.pop(0)
            sum += node.val
            
            if node.left is not None:
                q.append(node.left)

            if node.right is not None:
                q.append(node.right)

            count -= 1

        if sum < min_sum:
            min_sum = sum
            min_level = level

        level += 1

    return min_level, min_sum


#root = Node(1) # trivial test case

#root = None # edge case

# root = Node(5)
# l = root.left = Node(3)
# ll = l.left = Node(1)
# lr = l.right = Node(4)
# lll = ll.left = Node(0)
# r = root.right = Node(7)
# rl = r.left = Node(6)
# rr = r.right = Node(9)
# rrl = rr.left = Node(8)

root = Node(10)
l = root.left = Node(5)
lr = l.right = Node(2)
r = root.right = Node(5)
rr = r.right = Node(1)
rrl = rr.left = Node(-1)

print_tree(root)

min_level, min_sum = level_with_min_sum(root)
print("min level = {}, min sum = {}".format(min_level, min_sum))


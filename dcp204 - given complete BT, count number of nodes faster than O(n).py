"""
dcp#204

This problem was asked by Amazon.

Given a complete binary tree, count the number of nodes in faster than O(n) time. Recall that a complete binary tree has every level filled except the last, and the nodes in the last level are filled starting from the left.

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
    print("  "*depth, root.val)
    print_tree(root.left, depth + 1)

###############################################################################

# Solution #1
# For general binary tree--doesn't assume it's complete.
# O(n)
def count_nodes(root, count=0):
    if root is None:
        return 0

    count += 1 + count_nodes(root.left) + count_nodes(root.right)

    return count

###############################################################################

def left_height(root):
    h = 0

    while root is not None:
        root = root.left
        h += 1

    return h

def right_height(root):
    h = 0

    while root is not None:
        root = root.right
        h += 1
    
    return h

# Solution #2
# Assume complete binary tree.
# Height here is 1-based.
# Overall time: O(h^2) = O((log n)^2), where h is height of tree.
# First call is ~h.  IF needed, second call is h-1.  Etc.
# Worst case: h + (h - 1) + ... + 1 = O(h^2).
def count_nodes2(root):
    if root is None:
        return 0
    
    lh = left_height(root)
    rh = right_height(root)

    if lh == rh:
        return (1 << lh) - 1 # height here is 1-based

    return count_nodes2(root.left) + count_nodes2(root.right) + 1


###############################################################################

# For count_nodes2().
# Does binary search for last element of complete binary tree.
# Essentially treats last level of tree like an array in binary search.
# Returns index of last element on last level of tree.
def find_last_elt(root, depth, start, end):
    if start > end:
        return start - 1

    mid = (start + end) // 2
    node = root
    print("\nrange = {}, {}".format(start, end))
    print("mid start = {}".format(mid))

    # number of bits to consider = depth of tree
    path = mid
    for i in range(depth - 1, -1, -1):
        print("bit = (path >> i) & 1 = {}".format((path >> i) & 1))
        if (path >> i) & 1: # ith bit is 1
            node = node.right
        else: # ith bit is 0
            node = node.left

    if node is None:
        print("node is None.")
    else:
        print("node value = {}".format(node.val))

    if node is None:
        return find_last_elt(root, depth, start, mid - 1)
    else:
        return find_last_elt(root, depth, mid + 1, end)


# Solution #3: use binary search on last level of tree.
# Assume complete binary tree.
# See example below.
# Overall O((log n)^2) time.
# O(log n) each time the tree is traversed.
# O(log n) to do binary search on last level.
def count_nodes3(root, count=0):
    depth = -1
    node = root

    # Root of tree is at depth 0.
    while node is not None:
        node = node.left
        depth += 1

    # Perfect tree of depth d has 2**(d+1) - 1 elements.
    # Complete tree exlcuding last level is perfect.
    # Here, count of nodes at all but last level.
    count = 2**depth - 1
    print("depth = {}, count = {}".format(depth, count))

    # Now need to count elements in last level.
    # Idea: do some kind of binary search to check where last elt is.
    # Max number of elements on last level also happens to be count+1.

    last_index = find_last_elt(root, depth, start=0, end=count)

    return count + last_index + 1


"""
           1
        /     \
     2           3
    /  \        /  \
  4     5      6     7
 / \   / \    / \    /  \
8   9 10 11  12 13  14   15

Assume not all elements of last level are actually there.
Root (1) is at depth = 0.
Depth of tree = 3.

//////////////////
Example for count_nodes2(), which uses binary search:

kth node at bottom level, k = 0, 1, 2, ...
Express k in binary.
Bits in binary rep of k shows how to go down tree to get to kth node,
where bit 0 means go left, and bit 1 means go right.
Number of bits = height of last level (here, 3).

k = 0: 0b000 = LLL = 8
k = 1: 0b001 = LLR = 9
k = 2: 0b010 = LRL = 10
k = 3: 0b011 = LRR = 11
k = 4: 0b100 = RLL = 12
k = 5: 0b101 = RLR = 13
k = 6: 0b110 = RRL = 14
k = 7: 0b111 = RRR = 15

Binary search of last level.
Range is k in [0, 7].  Last = 2^h - 1 = 7, where h = 3.

First try (0 + 7) // 2 = 3.
If k = 3 found, then look in range [k+1, 7] = [4, 7].
    Try (4 + 7) // 2 = 5.  Etc.
If k = 3 NOT found, then look in range [0, k-1] = [0, 2].
    Try (0 + 2) // 2 = 1.  Etc.


"""

# import sys
# recursion_limit = sys.getrecursionlimit()
# print("Recursion limit = {}".format(recursion_limit))
# print("Setting it to 10.\n")
# sys.setrecursionlimit(10)

root = Node(1)
l = root.left = Node(2)
r = root.right = Node(3)
ll = l.left = Node(4)
lr = l.right = Node(5)
rl = r.left = Node(6)
rr = r.right = Node(7)
ll.left = Node(8)
ll.right = Node(9)
lr.left = Node(10)
lr.right = Node(11)
rl.left = Node(12)
rl.right = Node(13)
#rr.left = Node(14)
#rr.right = Node(15)

#n = count_nodes(root)
n = count_nodes2(root)
#n = count_nodes3(root)

print()
print_tree(root)

print("\nNumber of nodes = {}".format(n))


"""
dcp#133

This problem was asked by Amazon.

Given a node in a binary search tree, return the next bigger element, also known as the inorder successor.

For example, the inorder successor of 22 is 30.

   10
  /  \
 5    30
     /  \
   22    35
You can assume each node has a parent pointer.
"""

# Clarify: are we given just the key value or the actual node?

class Node():
    def __init__(self, val, parent=None, left=None, right=None):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right
        

def print_tree(root, depth=0):
    if root is None:
        return

    print_tree(root.right, depth + 1)
    print("  "*depth + str(root.val))
    print_tree(root.left, depth + 1)


################################################################################
# Solution #1
# Do an in-order traversal until given value is found, then return next node.
# Doesn't use parent pointers.
# Assume given value k can be found in BST.
def next_node(root, k, flag=[]):
    if root is None:
        return None

    result = next_node(root.left, k, flag)
    if result is not None:
        return result
    
    if len(flag) > 0:
        return root

    if root.val == k:
        flag.append(True)

    return next_node(root.right, k, flag)


################################################################################
# Solution#2: use parent pointer
# If node has right child, then go right, then all the way to left to get next value.
# If node has no right child, then look at parent.
#       If node has no parent, then it must be root, and there is no bigger element.
#       If node has parent, and node is parent's left child, then parent is next node.
#       Otherwise, keep tracing parents until traverse a parent through its left child.
#           This parent is the next node.
# Assume: given node is not empty.
def next_node2(node):
    # if node is None:
    #     return None

    if node.right is not None:
        node = node.right
        while node.left is not None:
            node = node.left

        return node

    # otherwise, root has no right child, so look at parents
    while node.parent is not None:
        if node.parent.left == node:
            return node.parent

        node = node.parent
        
    return None

# Find and return node with value k, given BST root.
def find(root, k):
    if root is None:
        return None

    if root.val == k:
        return root
    elif root.val < k:
        return find(root.right, k)
    else:
        return find(root.left, k)


################################################################################
# Solution #3:
# If right subtree of given node exists, then go right, then all the way left.
# Otherwise, start from root of BST and search...
# Doesn't use parent pointers.
def next_node3(root, node):
    if node.right is not None:
        node = node.right
        while node.left is not None:
            node = node.left

        return node

    # otherwise, root has no right child, so start from root
    next = None

    while root is not None:
        if root.val < node.val:
            root = root.right
        elif root.val > node.val:
            next = root
            root = root.left
        else:
            break

    return next


################################################################################

def print_result(next):
    if next is None:
        print("\nGiven node is last element in BST")
    else:
        print("\nNext value: {}".format(next.val))

root = Node(10)
l = root.left = Node(5, root)
r = root.right = Node(30, root)
rl = r.left = Node(22, r)
rr = r.right = Node(35, r)

print_tree(root)

k = 10 # Assume given value k can be found in BST.
print("\nGiven value: {}".format(k))

next = next_node(root, k)
print_result(next)

################################################################################

print("\n### Testing solution #2")

node = find(root, k)
if node is None:
    print("\nNode value {} not found.".format(k))
else:
    print("\nNode value found: {}".format(node.val))

next = next_node2(node)
print_result(next)

################################################################################

print("\n### Testing solution #3")

next = next_node3(root, node)
print_result(next)


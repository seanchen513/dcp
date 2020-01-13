"""
This problem was asked by Google.

Given the root of a binary search tree, and a target K, return two nodes in the tree whose sum equals K.

For example, given the following tree and K of 20

    10
   /   \
 5      15
       /  \
     11    15
Return the nodes 5 and 15.
"""

# Clarify: do the two nodes returned have to be different nodes?
# Assume yes since the given example returns 5 and 15 rather than 10 and 10.

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


################################################################################
# Solution #1: use dict to keep track of values/nodes found
# O(n) time somce doing in-order traversal of BST
# O(n) space due to found_dict
def find_nodes(root, sum, pair_found, found_dict={}):
    if root is None:
        return False
    
    if find_nodes(root.left, sum, pair_found, found_dict):
        return True

    if (sum - root.val) in found_dict:
        #print("FOUND: {}".format(root.val))
        pair_found.append(root)
        pair_found.append(found_dict[sum - root.val])
        return True
    else:
        found_dict[root.val] = root
    
    return find_nodes(root.right, sum, pair_found, found_dict)
        

################################################################################
# Solution #2: do in-order traversal of BST and store values in array
# O(n) time
# O(n) space due to array
def find_nodes2(root, target, pair_found):
    lst = []
    tree_to_list(root, lst)

    start = 0
    end = len(lst) - 1

    while start < end:
        sum = lst[start].val + lst[end].val
        if sum == target:
            pair_found.append(lst[start])
            pair_found.append(lst[end])
            return True
        elif sum < target:
            end -= 1
        elif sum > target:
            start += 1

    return False

# helper function for find_nodes2()
def tree_to_list(root, lst):
    if root is None:
        return

    tree_to_list(root.left, lst)
    lst.append(root)
    tree_to_list(root.right, lst)


################################################################################
# Solution #3: convert BST to sorted doubly-linked list in-place
# O(n) time
# O(log n) space, but modifies BST



################################################################################
# Solution #4: traverse in in-order and reverse in-order at same time.  uses stacks.
# O(n) time
# O(log n) space -- DOES NOT modify BST




################################################################################

root = Node(10)
l = root.left = Node(5)
r = root.right = Node(15)
rl = r.left = Node(11)
rr = r.right = Node(15)

print_tree(root)

k = 20
pair_found = []
#found = find_nodes(root, k, pair_found)
found = find_nodes2(root, k, pair_found)

print("\nsum = {}".format(k))

if found:
    print("nodes: {}, {}".format(pair_found[0].val, pair_found[1].val))
else:
    print("No two distinct nodes found that add up to given sum.")


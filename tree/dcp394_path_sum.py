"""
dcp#394

This problem was asked by Uber.

Given a binary tree and an integer k, return whether there exists a root-to-leaf path that sums up to k.

For example, given k = 18 and the following binary tree:

    8
   / \
  4   13
 / \   \
2   6   19

Return True since the path 8 -> 4 -> 6 sums to 18.
"""

"""
112. Path Sum
Easy

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.
"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def array_to_bt(arr):
    n = len(arr)
    nodes = [None] * n

    for i in range(n):
        if arr[i] is not None:
            nodes[i] = TreeNode(arr[i])
            
    for i in range(n//2):
        if arr[2*i + 1] is not None:
            nodes[i].left = nodes[2*i + 1]

        if arr[2*i + 2] is not None:
            nodes[i].right = nodes[2*i + 2]

    return nodes[0]

def print_tree(root, depth=0):
    if root is None:
        return

    print_tree(root.right, depth + 1)
    print("  "*depth + str(root.val))
    print_tree(root.left, depth + 1)

###############################################################################
"""
Solution #1: recursion

Finds the first leaf that gives the target sum along the path from root to leaf
"""
def path_target_sum(root, target_sum, sum=0):
    if root is None:
        return None

    sum += root.val

    if not root.left and not root.right and sum == target_sum:
        return root
    
    leaf = path_target_sum(root.left, target_sum, sum)
    if leaf:
        return leaf

    leaf = path_target_sum(root.right, target_sum, sum)
    if leaf:
        return leaf

"""
Solution #2: same but decrement target_sum instead of passing path_sum.
"""
def path_target_sum2(root, target_sum):
    if root is None:
        return None

    target_sum -= root.val

    if not root.left and not root.right and target_sum == 0:
        return root
    
    leaf = path_target_sum2(root.left, target_sum)
    if leaf:
        return leaf

    leaf = path_target_sum2(root.right, target_sum)
    if leaf:
        return leaf

###############################################################################

def path_to_node(root, node):
    # define inner path_dfs() so path variable is initialized to [] each time
    # path_to_node() is called.
    def path_dfs(root, node, path=[]):
        if root is None:
            return None

        if root == node or path_dfs(root.left, node) or path_dfs(root.right, node):
            path.append(root.val)
            return path

        return None

    # path = [] # can also do this instead of having "path=[]" in path_dfs()
    return path_dfs(root, node)


# Alternative
def path_to_node2(root, node, path=None):
    if path is None: # mutable so don't use default arg [] for path
        path = [] # create new object each time fn is called outside recursion

    if root is None:
        return None

    if (root == node 
        or path_to_node2(root.left, node, path) 
        or path_to_node2(root.right, node, path)
    ):
        path.append(root.val)
        return path

    return None

###############################################################################

if __name__ == "__main__":
    def test(root, target_sum):
        leaf = path_target_sum(root, target_sum)
        #leaf = path_target_sum2(root, target_sum)
        
        print("\n" + "#"*80)
        print_tree(root)
        print(f"\ntarget sum = {target_sum}")

        if leaf is None:
            print("\nNo path from root to leaf that sums to given number.")
        else:
            print(f"\nleaf = {leaf.val}")

        path = path_to_node(root, leaf)
        print(f"\npath = {path}")

    ### dcp394 example
    root = TreeNode(8)
    root.left = TreeNode(4)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(6)
    root.right = TreeNode(13)
    root.right.right = TreeNode(19)

    target_sum = 18
    test(root, target_sum)

    ### LC113. example
    arr = [5,4,8,11,None,13,4,7,2,None,None,None,None,5,1] 
    root = array_to_bt(arr)
    target_sum = 22

    test(root, target_sum)

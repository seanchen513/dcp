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

"""
257. Binary Tree Paths
Easy

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
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

Use inner function so path and paths are initialized each time
outer function is called.

Note that "path" is mutable and we have to pass it to the left and right
subtrees, so create a new copy for each node.
"""
def all_paths(root):
    def dfs(node, path=[], paths=[]):
        if not node:
            return paths

        #path.append(node.val) # doesn't work
        path = path + [node.val] # create new object

        if not node.left and not node.right:
            paths.append(path)

        paths = dfs(node.left, path, paths)
        paths = dfs(node.right, path, paths)
        
        return paths

    return dfs(root)

"""
Same as all_paths() but return in LC format.

Example: ["1->2->5", "1->3"]
"""
def all_paths_lc(root):
    def dfs(node, path="", paths=[]):
        if not node:
            return paths

        #path.append(node.val) # doesn't work
        #path = path + [node.val] # create new object
        if path == "":
            path = str(node.val)
        else:
            path += "->" + str(node.val)

        if not node.left and not node.right:
            paths.append(path)

        paths = dfs(node.left, path, paths)
        paths = dfs(node.right, path, paths)
        
        return paths

    return dfs(root)

###############################################################################
"""
Solution #2: recursion with list comprehensions.
No extra function parameters.
"""
def all_paths2(root):
   if not root: 
       return []
   
   if not root.left and not root.right: 
       return [[root.val]]
   
   return [[root.val] + i for i in all_paths2(root.left)] + \
             [[root.val] + i for i in all_paths2(root.right)]


"""
LC format
"""
def all_paths_lc2(root):
   if not root: 
       return []
   
   if not root.left and not root.right: 
       return [str(root.val)]
   
   return [str(root.val) + '->' + i for i in all_paths_lc2(root.left)] + \
             [str(root.val) + '->' + i for i in all_paths_lc2(root.right)]

###############################################################################

if __name__ == "__main__":
    def test(root):
        print("\n" + "#"*80)
        print_tree(root)
        
        #paths = all_paths(root)
        #paths = all_paths_lc(root)
        paths = all_paths2(root)
        #paths = all_paths_lc2(root)
        
        print()
        print(paths)

    root = None
    test(root)

    root = TreeNode(1)
    test(root)

    arr = [1, 2, 3, None,None,4,5]
    root = array_to_bt(arr)
    test(root)

    root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5)))))
    test(root)

    arr = [1, 2,3, 4,5,6,7]
    root = array_to_bt(arr)
    test(root)

    # LC example
    arr = [1, 2,3, None,5,None,None]
    root = array_to_bt(arr)
    test(root)

'''
dcp#3

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

'''

class Node
    def __init__(self, val, left=None, right=None)
        self.val = val
        self.left = left
        self.right = right


# serializes binary tree specified by root into a string
# pre-order traversal
def serialize(root)
    if root is None
        return  # is none or null better
    else
        return root.val + . + serialize(root.left) + . + serialize(root.right)


# deserializes string representing a binary tree into a binary tree (represented by root node)
def deserialize(str)
    n = Node(None)
    vals = str.split('.')
    for val in vals
        
    if str[0] != .
        n = Node[str[0]]


node = Node('root', Node('left', Node('left.left')), Node('right'))
#assert deserialize(serialize(node)).left.left.val == 'left.left'

node = (Node('1',
    Node('2', Node('4'), Node('5')), 
    Node('3', Node('6'), Node('7'))
    ))

print(serialize(node))

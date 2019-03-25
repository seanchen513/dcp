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

class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

################################################################################
### For node values that are single characters.

# Pre-order traversal.
# Use '/' for null nodes.

def serialize(root):
    if root is None:
        return ''

    if root.left is not None:
        if root.right is not None:
            return root.val + serialize(root.left) + serialize(root.right)
        else:
            return root.val + serialize(root.left) + '/'    
    else:
        if root.right is not None:
            return root.val + '/' + serialize(root.right) 
        else:
            return root.val + '//'


def deserialize(str, k, root):
    if (k >= len(str)) or (str[k] == '/'):
        k += 1
        return k, None

    root = Node(str[k])
    k += 1

    k, root.left = deserialize(str, k, root.left)
    k, root.right = deserialize(str, k, root.right)
    return k, root


################################################################################
### For node values that are single characters.

# Serializes binary tree specified by root into a string.
# Pre-order traversal with non-leaves followed by '#' and
# null children of non-leaves followed by '/' 

def serialize2(root):
    if root is None:
        return ''

    if root.left is not None:
        if root.right is not None:
            return root.val + '#' + serialize2(root.left) + serialize2(root.right)
        else:
            return root.val + '#' + serialize2(root.left) + '/'    
    else:
        if root.right is not None:
            return root.val + '#/' + serialize2(root.right) 
        else:
            return root.val


def deserialize2(str, k, root):
    if (k >= len(str)) or (str[k] in '/#'):
        k += 1
        return k, None

    root = Node(str[k])
    k += 1

    k, root.left = deserialize2(str, k, root.left)
    k, root.right = deserialize2(str, k, root.right)
    return k, root

################################################################################
### Generalize so values of nodes can be more than one character long.

# Pre-order traversal.
# Use '$' to indicate end of value.
# Use '/' for null nodes.

def serialize3(root):
    if root is None:
        return ''

    if root.left is not None:
        if root.right is not None:
            return root.val + '$' + serialize3(root.left) + serialize3(root.right)
        else:
            return root.val + '$' + serialize3(root.left) + '/'    
    else:
        if root.right is not None:
            return root.val + '$/' + serialize3(root.right) 
        else:
            return root.val + '$//'


def deserialize3(str, k, root):
    if (k >= len(str)) or (str[k] == '/'):
        k += 1
        return k, None

    end = str.find('$', k)
    s = str[k:end]
    k = end + 1

    # s = ''
    # while (k < len(str)):
    #     ch = str[k]

    #     if ch == '$':
    #         k += 1
    #         break

    #     s += ch
    #     k += 1

    root = Node(s)

    k, root.left = deserialize3(str, k, root.left)
    k, root.right = deserialize3(str, k, root.right)
    return k, root


################################################################################
### For testing.

def preorder(root):
    if root is not None:
        print(root.val, end=' ')
        preorder(root.left)
        preorder(root.right)

def deser(str):
    root = None
    _, root = deserialize(str, 0, root)
    return root

# node = Node('root', Node('left', Node('left.left')), Node('right'))
# print(deser(serialize(node)).left.left.val)
# assert deser(serialize(node)).left.left.val == 'left.left'

################################################################################


# node = (Node('1',
#     Node('2', Node('4'), Node('5')), 
#     Node('3', Node('6'), Node('7'))
#     ))

# node = Node('A')
# node.left = Node('B')
# node.left.left = Node('D')
# node.left.right = Node('E')
# node.left.right.left = Node('G')
# node.right = Node('C')
# node.right.right = Node('F')

node = Node('Apple')
node.left = Node('Banana')
node.left.left = Node('Donut')
node.left.right = Node('Egg')
node.left.right.left = Node('Grape')
node.right = Node('Carrot')
node.right.right = Node('Fruit')

print("\nPre-order traversal before serialization: ")
preorder(node)

#ser = serialize(node)
#ser = serialize2(node)
ser = serialize3(node)

print("\n\nSerialized:")
print(ser)

root = None
#k, root = deserialize(ser, 0, root)
#k, root = deserialize2(ser, 0, root)
k, root = deserialize3(ser, 0, root)

print("\nPre-order traversal of deserialized: ")
preorder(root)


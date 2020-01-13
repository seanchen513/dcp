"""
dcp020
dip023

This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

"""

# Naive method is O(M*N): nested loops...


class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}, {self.next.__repr__()}"


"""
Solution#1: mark visited nodes.
Instead of modifying the nodes, we use a set.
O(M + N) time
O(M + N) space...
"""
def intersecting_node(a, b):
    visited = set()

    while a:
        visited.add(a)
        a = a.next

    while b:
        if b in visited:
            return b
        
        visited.add(b)
        b = b.next

    return None


"""
# Solution#2: use difference of node counts.
Assume that starting with the first intersecting node, both
lists share all remaining nodes.

Traverse longer list first by |M - N| nodes.  
Then traverse both lists in parallel.
The parallel traversals will arrive at the first intersecting
node at the same time.

O(M + N) time
O(1) space
"""
def intersecting_node2(a, b):
    ### Find lengths of each list.

    len_a = 0
    temp = a
    while temp:
        len_a += 1
        temp = temp.next

    len_b = 0
    temp = b
    while temp:
        len_b += 1
        temp = temp.next

    ### Traverse longer list by difference in lengths of lists.
    
    d = abs(len_a - len_b)
    if len_a >= len_b:
        for _ in range(d):
            a = a.next
    else:
        for _ in range(d):
            b = b.next

    ### Parallel traversal of both lists.

    while a != b:
        a = a.next
        b = b.next

    return a


###############################################################################

c = Node(8, Node(10))
a = Node(3, Node(7, c))
b = Node(99, Node(1, c))
#b = Node(99, Node(1, Node(2, Node(3))))

print(a)
print(b)

node = intersecting_node(a, b)

print(node)


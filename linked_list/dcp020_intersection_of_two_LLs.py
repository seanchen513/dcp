"""
dcp020
dip023

This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
"""

"""
LC160. Intersection of Two Linked Lists
Easy

Write a program to find the node at which the intersection of two singly linked lists begins.

....

Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""

class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}, {self.next.__repr__()}"

"""
Brute force solution using nested loops.

O(m*n) time
O(1) extra space
"""
# Not done

"""
Solution #1: mark visited nodes.
Instead of modifying the nodes, we use a set.

O(m+n) time
O(m+n) extra space
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
Solution #2: use difference of node counts (list lengths).

Assume that starting with the first intersecting node, both
lists share all remaining nodes.

First, traverse longer list first by |M - N| nodes.  
Then traverse both lists in parallel.
The parallel traversals will arrive at the first intersecting
node (if there is one, otherwise None) at the same time.

O(m + n) time
O(1) extra space
Input lists are not modified.
"""
def intersecting_node2(a, b):
    ### 1. Find lengths of each list.

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

    ### 2. Traverse longer list by difference in lengths of lists.
    
    if len_a >= len_b:
        for _ in range(len_a - len_b):
            a = a.next
    else:
        for _ in range(len_b - len_a):
            b = b.next

    ### 3. Simultaneous traversal of both lists.

    while a != b:
        a = a.next
        b = b.next

    return a

"""
Solution #3: Simultaneous traversal of combined lists a -> b and b -> a.
These both have the same length.  If there is an intersecting node,
then both a and b share some sublist at their ends.  So the combined lists
share that same sublist at their ends.  If there is no intersecting node,
then both pointers will arrive at None at the same time.

O(m+n) time
O(1) extra space
Input lists are not modified.
"""
def intersecting_node3(head_a, head_b):
    a = head_a
    b = head_b

    while a != b:
        if a:
            a = a.next
        else:
            a = head_b

        if b:
            b = b.next
        else:
            b = head_a

    return a

###############################################################################

if __name__ == "__main__":
    def test(a, b):        
        print(f"\na: {a}")
        print(f"b: {b}")
        
        node1 = intersecting_node(a, b) # use set
        node2 = intersecting_node2(a, b) # use diff in list lengths
        node3 = intersecting_node3(a, b) # simult traversal of a->b and b->a

        print(f"intersection (use set)             : {node1}")
        print(f"intersection (diff in list lengths): {node2}")
        print(f"intersection (a->b and b->a)       : {node3}")

    ### a and b intersect at c
    c = Node(8, Node(10))
    a = Node(3, Node(7, c))
    b = Node(99, Node(1, c))
    test(a, b)
    
    ### lists of different lengths
    b = Node(-1, Node(-2, Node(-3, Node(-4, c))))
    test(a, b)

    ### intersection is at start of b (ie, b is sublist of a)
    b = c
    test(a, b)

    ### intersection is last node of both lists
    last = Node(999)
    x = Node(1, Node(2, last))
    y = Node(3, Node(4, Node(5, last)))
    test(x, y)

    ### intersection is first node of both lists (ie, both lists are same)
    test(x, x)

    ### both lists are the same 1-length lists.
    test(last, last)

    ### a and b do not intersect
    b = Node(-1, Node(-2, Node(-3, Node(-4))))
    test(a, b)

    ### one list is None
    test(a, None)

    ### both lists are None
    test(None, None)

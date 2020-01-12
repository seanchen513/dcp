"""
dcp145

This problem was asked by Google.

Given the head of a singly linked list, swap every two nodes and return its head.

For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.

"""


class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}, {self.next.__repr__()}"


"""
Solution#1: iterative.
Note that node values are not swapped between nodes.
We modify links between nodes.
"""
def swap_nodes(head):
    if (head is None) or (head.next is None):
        return head

    node = head
    head = head.next
    prev = None

    while node and node.next:   # Example: node = 1 -> 2 -> 3 -> ...
        temp = node.next        # temp = 2
        node.next = temp.next   # 1.next = 3
        temp.next = node        # 2.next = 1
        
        if prev:
            prev.next = temp

        prev = node
        node = node.next        # node = 1.next = 3

    return head


"""
Solution#2: recursive
"""
def swap_nodes2(head):
    if (head is None) or (head.next is None):
        return head

    # Example in comments for head = 1 -> 2 -> 3 -> ...
    temp = head.next        # temp = 2
    head.next = temp.next   # 1.next = 3
    temp.next = head        # 2.next = 1
    head = temp             # head = 2

    head.next.next = swap_nodes2(head.next.next)

    return head


###############################################################################

head = Node(1)
head = Node(1, Node(2))
#head = Node(1, Node(2, Node(3)))
#head = Node(1, Node(2, Node(3, Node(4))))
#head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))

print(f"\n{head}")

print("\nSwapping nodes pairwise (iterative):")
head = swap_nodes(head)
print(head)

print("\nSwapping nodes pairwise (recursive) to get back original linked list:")
head = swap_nodes(head)
print(head)


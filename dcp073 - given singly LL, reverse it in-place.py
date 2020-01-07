"""
dcp#73

This problem was asked by Google.

Given the head of a singly linked list, reverse it in-place.
"""

class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}, {self.next.__repr__()}"


# Build singly linked list of length k, with values 1 through k
# Returns both head and tail
def build_ll(k):
    if k == 0:
        return None, None

    head = Node(1)
    tail = head

    for i in range(2, k+1):
        tail.next = Node(i)
        tail = tail.next

    return head, tail


###############################################################################

# Reverses singly linked list in-place.
# O(n) time.
def reverse_ll(head):
    ### Not necessary since these cases are dealt with correctly
    # if (head is None) or (head.next is None):
    #     return head

    lag = None
    scout = head

    # start of each loop: head = scout, and lag is behind by one node
    while scout is not None: 
        scout = scout.next # store this because head.next will be modified
        head.next = lag # reverse "next" pointer
        
        # advance the pointers without using "next" fields
        lag = head
        head = scout

    return lag

"""
Example:

1 -> 2 -> 3 -> 4 -> 5
              lag  scout = head

Want:
1 <- 2 <- 3 <- 4 <- 5

scout = 5
head = 5
lag = 4

next loop:
scout = None
head.next = 4 (5 -> 4)
lag = 5
head = None

return lag (5)

"""


###############################################################################

head = None
head, tail = build_ll(0) # None
head, tail = build_ll(1) # 1
head, tail = build_ll(2) # 1, 2
head, tail = build_ll(3) # 1, 2, 3
head, tail = build_ll(9) # 1, 2, 3, 4, 5, 6, 7, 8, 9

print("\nLinked list:")
print(head)

head = reverse_ll(head)
print("\nReversed linked list:")
print(head)


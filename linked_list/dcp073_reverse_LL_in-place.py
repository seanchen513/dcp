"""
dcp073

This problem was asked by Google.

Given the head of a singly linked list, reverse it in-place.
"""

"""
LC206. Reverse Linked List
Easy

Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}, {self.next.__repr__()}"

"""
Build singly linked list of length k, with values 1 through k.
Returns both head and tail.
"""
def build_ll_k(k):
    if k == 0:
        return None, None

    head = Node(1)
    tail = head

    for i in range(2, k+1):
        tail.next = Node(i)
        tail = tail.next

    return head, tail

###############################################################################
"""
Reverses singly linked list in-place.
O(n) time
O(1) space
"""
def reverse_ll(head):
    ### Not necessary since these cases are dealt with correctly
    # if (head is None) or (head.next is None):
    #     return head
    
    tail = head # for return; not needed for algo
    lag = None
    
    # start of each loop: head = scout, and lag is behind by one node
    while head:
        # temp var to hold head.next, because head.next will be modified
        scout = head.next

        # reverse "next" pointer
        head.next = lag 
        
        # advance the pointers without using "next" fields
        lag = head
        head = scout

    return lag, tail

"""
Example:

1 <- 2 <- 3 <- 4 -> 5
              lag  scout = head

start of loop:
    scout = 5
    head = 5
    lag = 4

scout = scout.next = None
head.next = lag = 4 (5 -> 4)
lag = head = 5
head = scout = None

return lag (5)
"""

###############################################################################
"""
Solution #2: recursive
"""
def reverse_ll_rec(head):
    if (head is None) or (head.next is None):
        return head, None

    if head.next.next is None:
        scout = head.next
        scout.next = head
        head.next = None
        return scout, head

    rev, tail = reverse_ll_rec(head.next)

    tail.next = head
    tail = head

    head.next = None

    return rev, tail

###############################################################################

if __name__ == "__main__":
    lists = [
        0, # None
        1, # 1 -> None
        2, # 1 -> 2 -> None
        3,
        9,
    ]

    for k in lists:
        head, _ = build_ll_k(k)
        head2, _ = build_ll_k(k)

        print(f"\nLinked list:\t{head}")
        
        rev, _ = reverse_ll(head)
        rev2, _ = reverse_ll_rec(head2)
        print(f"Reversed:\t{rev}")
        print(f"Recursive:\t{rev2}")

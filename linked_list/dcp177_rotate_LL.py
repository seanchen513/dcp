"""
dcp177

This problem was asked by Airbnb.

Given a linked list and a positive integer k, rotate the list to the right by k places.

For example, given the linked list 7 -> 7 -> 3 -> 5 and k = 2, it should become 3 -> 5 -> 7 -> 7.

Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 3, it should become 3 -> 4 -> 5 -> 1 -> 2.

"""

class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}, {self.next.__repr__()}"


# 0 <= k < length of linked list
def rotate_right(head, k):
    if (head is None) or (k == 0):
        return head

    if k < 0:
        print("\n### Need: 0 <= k < length of linked list")
        return

    orig_head = head
    
    ### Find node that will be tail of rotated list.
    ### It's next node will be the new head.  Unlink these two nodes.

    temp = head

    i = 0
    while temp and (i < k - 1):
        temp = temp.next
        i += 1

    if (i != k - 1) or (temp.next is None): # k is too big
        print("\n### k is too big!  Need: 0 <= k < length of linked list")
        return None

    head = temp.next # head of rotated list
    temp.next = None # temp is tail of roated list, so unlink it from new head

    ### Find tail of original list, and link it to original head.

    temp = head
    while temp and temp.next:
        temp = temp.next

    temp.next = orig_head

    return head


#head = Node(1)
#head = Node(1, Node(2))
head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
k = 2

print(f"\n{head}")

head = rotate_right(head, k)

print(f"\n{head}")


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

def get_length(head: Node) -> int:
    count: int = 0

    while head:
        count += 1
        head = head.next

    return count

"""
Rotate linked list to right by k elements.
Note that the last k nodes are moved to the front.
"""
def rotate_right(head: Node, k: int) -> Node:
    if head is None:
        return None

    k %= get_length(head)

    if k == 0:
        return head

    # Suppose there are n nodes, and we increment fast by k nodes first.
    # Then we increment both fast and slow until fast is the tail.
    # The pointers will have moved n - k - 1 nodes.
    # This means slow is at the (n - k)th node, and there are k nodes
    # after it.
    fast = head # will be tail of original linked list
    slow = head # will be node before head of new list, and tail of new list
    
    for _ in range(k): # k replaced by n-k to rotate left
        fast = fast.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    fast.next = head
    head = slow.next
    slow.next = None

    return head

"""
Example: rotate right

k = 2
1 2 3 4 5 6
S   F

1 2 3 4 5 6
      S   F

6.next = head = 1
head = slow.next = 5
3.next = None

5 6 1 2 3 4
"""

###############################################################################
"""
Rotate linked list to left by k elements.
Note that the first k elements are moved to the back.
"""
def rotate_left(head: Node, k: int) -> Node:
    return rotate_right(head, -k)

"""
Example: rotate left

k = 2
increment F by n - k = 6 - 2 = 4
1 2 3 4 5 6 
S       F

increment F and S until F is at tail:
1 2 3 4 5 6 
  S       F

fast.next = head # 6.next = 1
head = slow.next # head = 3
slow.next = None # 2.next = None

want:
3 4 5 6 1 2
"""

###############################################################################
"""
Original solution for rotate_left().
One pass.
0 <= k < length of linked list
"""
def rotate_left_old(head: Node, k: int) -> Node:
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

###############################################################################

if __name__ == "__main__":
    start = -4

    for k in range(start, 7):
        #head = None
        #head = Node(1)
        #head = Node(1, Node(2))
        head = Node(1, Node(2, Node(3, Node(4, Node(5)))))

        if k == start:
            print(f"\nOriginal linked list:\n{head}")

        head = rotate_right(head, k)
        #head = rotate_left(head, k)

        print(f"\nk = {k}: {head}")

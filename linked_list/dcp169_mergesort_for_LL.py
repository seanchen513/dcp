"""
dcp169

This problem was asked by Google.

Given a linked list, sort it in O(n log n) time and constant space.

For example, the linked list 4 -> 1 -> -3 -> 99 should become -3 -> 1 -> 4 -> 99.

"""


class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}, {self.next.__repr__()}"


def build_ll(it):
    if it is None:
        return None, None

    # works for dict and set, but it's probably not well-defined behavior
    if type(it) in [range, list]:
        it = iter(it)

    val = next(it, None)
    head = Node(val)
    tail = head
    
    val = next(it, None)
    while val is not None:
        tail.next = Node(val)
        tail = tail.next
        val = next(it, None)

    return head, tail


###############################################################################

def merge_sorted(l1, l2):
    if l2 is None:
        return l1
    
    if l1 is None:
        return l2

    if l1.val <= l2.val:
        l1.next = merge_sorted(l1.next, l2) 
        return l1
    else:
        l2.next = merge_sorted(l1, l2.next) 
        return l2


# Returns middle node (if odd number of nodes),
# or the left node of the two middle ones (if even number of nodes).
def get_middle(head):
    if head is None:
        return head

    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow


# Merge sort for linked list.
def ll_mergesort(head):
    if head is None or head.next is None:
        return head

    middle = get_middle(head)
    right = middle.next
    middle.next = None

    head = ll_mergesort(head) # left half
    right = ll_mergesort(right) # right half

    return merge_sorted(head, right)


###############################################################################


head = Node(4, Node(1, Node(-3, Node(99))))
head = Node(4)
head = None

head, _ = build_ll(range(9, 0, -1))
#head, _ = build_ll(range(1, 10))

print("\nLinked list:")
print(head)

head = ll_mergesort(head)

print("\nSorted:")
print(head)


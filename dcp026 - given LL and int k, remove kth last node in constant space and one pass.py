"""
dcp#398

This problem was asked by Amazon.

Given a linked list and an integer k, remove the k-th node from the end of the list and return the head of the list.

k is guaranteed to be smaller than the length of the list.

Do this in one pass.

"""


class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}, {self.next.__repr__()}"


# Assume k is integer >= 1, and <= length of linked list.
# O(n) time, one pass
def remove_kth_from_end(head, k):
    if k < 1:
        print("Given k must be an integer >= 1.")
        return head # don't modify linked list

    ### advance scout by k first
    scout = head

    while (k > 0) and (scout is not None):
        scout = scout.next
        k -= 1

    if scout is None: 
        if k > 0: # given k was longer than length of list
            print("Given k is too big (longer than length of linked list).")
            return head # don't modify linked list

        else: # k == 0; scout advanced exactly the length of linked list
            return head.next # removing 1st node

    ### scout is now ahead of head (lag) by k 
    lag = head

    while scout.next is not None:
        scout = scout.next
        lag = lag.next

    # scout is at end of list, and lag is k behind,
    # so lag is behind the node we want to remove.
    lag.next = lag.next.next

    return head


###############################################################################

head = Node(1, # 9th from end; k = 1 to remove it
    Node(2,
    Node(3,
    Node(4,
    Node(5,
    Node(6,
    Node(7,
    Node(8, # 2nd from end; k = 2 to remove it
    Node(9, # 1st from end
    )))))))))

k = 0 # error: k must be >= 1
k = 1 # should remove end of linked list
k = 9 # should remove current head node
k = 10 # error: k must be <= length of linked list

k = 3

print("\nLinked list:")
print(head)

print(f"\nk = {k}")

head = remove_kth_from_end(head, k)
print("\nAfter removing kth from end of linked list:")
print(head)


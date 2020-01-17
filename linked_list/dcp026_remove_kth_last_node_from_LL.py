"""
dcp26

This problem was asked by Google.

Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.

###############################################################################

dcp398

This problem was asked by Amazon.

Given a linked list and an integer k, remove the k-th node from the end of the list and return the head of the list.

k is guaranteed to be smaller than the length of the list.

Do this in one pass.
"""

"""
LC19. Remove Nth Node From End of List
Medium

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.

Follow up:
Could you do this in one pass?
"""

class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}, {self.next.__repr__()}"

"""
Solution:
Assume k is integer >= 1, and <= length of linked list.

O(n) time, one pass
"""
def remove_kth_from_end(head, k):
    # Advance scout by k first.
    scout = head

    for _ in range(k):
        scout = scout.next
    
    if scout is None: # k == length of list, so remove head node
        return head.next

    # scout is now ahead of head (lag) by k.
    lag = head

    while scout.next:
        scout = scout.next
        lag = lag.next

    # scout is at end of list, and lag is k behind,
    # so lag is behind the node we want to remove.
    lag.next = lag.next.next

    return head

"""
Same solution without assumptions about k.
"""
def remove_kth_from_end2(head, k):
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

if __name__ == "__main__":
    import copy
    def test(head, k):    
        print("#"*80)
        print(f"\n{head}")

        print(f"\nk = {k}, removing kth node from end:")
        
        head = remove_kth_from_end(head, k)
        #print("\nAfter removing kth from end:")
        print(head)
        print()


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

    #test(copy.deepcopy(head), 0) # error: k must be >= 1
    #test(copy.deepcopy(head), 10) # error: k must be <= length of linked list

    test(copy.deepcopy(head), 2)
    test(copy.deepcopy(head), 1) # should remove end of linked list
    test(copy.deepcopy(head), 9) # should remove current head node
    
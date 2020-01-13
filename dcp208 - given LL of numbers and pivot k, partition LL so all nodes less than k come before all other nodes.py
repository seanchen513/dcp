"""
dcp208

This problem was asked by LinkedIn.

Given a linked list of numbers and a pivot k, partition the linked list so that all nodes less than k come before nodes greater than or equal to k.

For example, given the linked list 5 -> 1 -> 8 -> 0 -> 3 and k = 3, the solution could be 1 -> 0 -> 5 -> 8 -> 3.
"""

class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}, {self.next.__repr__()}"


"""
Solution #1:
Every time a node with value < k is found, make it the new head.
May modify linked list even if all node values are < k.
O(n) time, O(1) space, single pass, NOT stable
"""
def segregate(head, k):
    node = head

    while node and node.next:
        #print(f"{node.val}, {node.next.val}")
        if node.next.val < k:
            temp = node.next.next
            node.next.next = head
            head = node.next
            node.next = temp
        else:
            node = node.next

    return head


"""
Solution #2:
Stable (relative order of elements is not changed.)
O(n) time, O(1) space.
"""
def segregate2(head, k):
    if head is None:
        return None

    bigger_head = None # nodes with values >= k
    bigger = None 
    
    node = head 

    while node and node.next:
        #print(f"node = {node}")
        if node.next.val >= k:
            if bigger is None:
                bigger_head = node.next
                bigger = node.next
            else:
                bigger.next = node.next
                bigger = bigger.next

            node.next = node.next.next
            bigger.next = None
            
        else:
            node = node.next

    """
    In general, node will now be tail of list of elements that didn't
    get moved, ie, the ones < k.  However, if all elements got moved,
    ie, all were < k, then node == head.
    """

    # Haven't checked head yet, so check it now.
    if head.val >= k: # then move this node to head of bigger
        temp = head.next
        head.next = bigger_head
        bigger_head = head
        head = temp

    # print(f"\nbigger_head = {bigger_head}")
    # print(f"head = {head}")
    # print(f"node = {node}")
    
    if head is None: # all elements were moved to bigger
        head = bigger_head
    else: # attach bigger list to tail of other list
        node.next = bigger_head

    return head


###############################################################################


print("\nAll nodes < k moved before all other nodes.")

for k in range(0, 7):
    #head = None
    #head = Node(1)
    
    #head = Node(1, Node(2))
    #head = Node(2, Node(1))

    #head = Node(5, Node(1, Node(8, Node(0, Node(3))))) # dcp
    head = Node(5, Node(4, Node(3, Node(2, Node(1)))))
    
    #head = segregate(head, k) # not stable
    head = segregate(head, k) # stable

    print(f"\nk = {k}: {head}")


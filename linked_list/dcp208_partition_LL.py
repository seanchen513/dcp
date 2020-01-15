"""
dcp208
LC86 medium

This problem was asked by LinkedIn.

Given a linked list of numbers and a pivot k, partition the linked list so that all nodes less than k come before nodes greater than or equal to k.

For example, given the linked list 5 -> 1 -> 8 -> 0 -> 3 and k = 3, the solution could be 1 -> 0 -> 5 -> 8 -> 3.
"""

"""
LeetCode:
You should preserve the original relative order of the nodes in each of the two partitions.
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
def partition(head: Node, k: int) -> Node:
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
This code can be simplified using dummy nodes (solution #3).
O(n) time, O(1) space.
"""
def partition2(head: Node, k: int) -> Node:
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

"""
Solution #3: Use dummy nodes to point to lists of smaller and larger nodes.
O(n) time, O(1) space
"""
def partition3(head: Node, k: int) -> Node:
    # dummy nodes
    smaller_head = Node(0)
    bigger_head = Node(0)
    
    smaller = smaller_head
    bigger = bigger_head
    node = head

    while node:
        if node.val < k:
            smaller.next = node
            smaller = smaller.next
        else:
            bigger.next = node
            bigger = bigger.next

        node = node.next

    bigger.next = None

    smaller.next = bigger_head.next

    return smaller_head.next

###############################################################################

if __name__ == "__main__":
    print("\nAll nodes < k moved before all other nodes.")

    for k in range(-1, 8):
        #head = None
        #head = Node(1)
        
        #head = Node(1, Node(2))
        #head = Node(2, Node(1))

        #head = Node(5, Node(1, Node(8, Node(0, Node(3))))) # dcp
        head = Node(5, Node(4, Node(3, Node(2, Node(1)))))
        
        #head = partition(head, k) # not stable
        #head = partition2(head, k) # stable
        head = partition3(head, k) # stable; use dummy nodes

        print(f"\nk = {k}: {head}")

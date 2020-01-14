"""
dcp078

This problem was asked recently by Google.

Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.

"""

import heapq

class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}, {self.next.__repr__()}"

    # Needed for sorted merge of k sorted linked lists.
    def __lt__(self, other):
        return self.val < other.val

"""
Build singly-linked list using values from given iterator "it".
Returns both head and tail.
"""
def build_ll(it) -> (Node, Node):
    if it is None:
        return None, None

    # works for dict and set, but it's probably not well-defined behavior
    if type(it) in [range, list]:
        it = iter(it)

    header = Node() # dummy header node
    tail = header

    val = next(it, None)
    while val:
        tail.next = Node(val)
        tail = tail.next
        val = next(it, None)

    return header.next, tail

###############################################################################

"""
Solution #1:
Use min heap to store heads of each list.
Assume function __lt__() has been defined in class Node.

O(n log k) time, where n = total number of elements among all input lists.
O(nk log k) time if all atomic lists have approx. length n.
"""
def sorted_merge(lists = list) -> Node:
    vals = []
    
    for ll in lists:
        if ll:
            vals.append(ll)
            #heapq.heappush(vals, ll)
    
    heapq.heapify(vals) # O(k)

    header = Node() # dummy header node
    tail = header

    while vals:
        m = heapq.heappop(vals) # O(log k)
        
        tail.next = m
        tail = tail.next

        if m.next:
            heapq.heappush(vals, m.next) # O(log k)

    return header.next, tail

"""
Solution #1b:
Same as solution #1 using min heap, 
BUT don't assume function __lt__() has been defined in class Node.
Deal with this by using storing tuples (node value, index of lists, node)
in heap rather than nodes.
"""
def sorted_merge1b(lists = list) -> Node:
    vals = []

    for i in range(len(lists)):
        if lists[i]:
            #vals.append((lists[i].val, i, lists[i]))
            heapq.heappush(vals, (lists[i].val, i, lists[i]))
    
    #heapq.heapify(vals) # O(k)

    header = Node() # dummy header node
    tail = header

    while vals:
        _, index, m = heapq.heappop(vals) # O(log k)
        
        tail.next = m
        tail = tail.next

        if m.next:
            heapq.heappush(vals, (m.next.val, index, m.next)) # O(log k)

    return header.next, tail

"""
Solution#2: 
Use array to store heads of each list.
Assume __lt__() is defined in class Node, but don't have to if
store tuples (node value, index of lists, node) in array.

Can either (1) sort array vals and extract vals[0] each time,
or (2) don't sort, but find min(vals) and remove it from array
each time.

O(nk) time, where n = total number of elements among all input lists.
O(n * k^2) time if all atomic lists have approx. length n.
"""
def sorted_merge2(lists = list) -> Node:   
    vals = []
    
    for ll in lists:
        if ll:
            vals.append(ll)
    
    header = Node() # dummy node
    tail = header

    while vals:
        # After first iteration, should be O(k) since we only appended one
        # item to sorted list.  First iteration is O(k log k).
        vals = sorted(vals)

        #m = min(vals)
        m = vals[0]
        
        tail.next = m
        tail = tail.next

        #vals.remove(m)
        vals = vals[1:]
        if m.next:
            vals.append(m.next)

    return header.next, tail

###############################################################################

"""
Sorted merge of l1 and l2, each of which is sorted.
Don't create a new list.
Iterative version.
O(n) time, O(1) space
"""
def merge_sorted(l1: Node, l2: Node) -> Node:
    header = Node() # dummy header for merged list
    node = header

    while l1 and l2:
        if l1.val <= l2.val:
            node.next = l1
            l1 = l1.next
        else:
            node.next = l2
            l2 = l2.next

        node = node.next

    if l1:
        node.next = l1
    elif l2:
        node.next = l2

    return header.next

"""
Solution #3: recursively merge 2 linked lists at a time.
O(n * k^2) time if all atomic lists have approx. length n.

Assume each atomic list has length n.
Merging sorted lists of lengths a and b is O(a+b).
The first merge is None with a list, which is O(1).

2n + 3n + ... + kn = n (2 + 3 + ... + k) = n[k(k+1)/2 - 1] = O(n * k^2)
"""
def sorted_merge_rec(lists : list) -> Node:
    merged = None

    for lst in lists:
        merged = merge_sorted(merged, lst)

    return merged

###############################################################################

import random

if __name__ == "__main__":
    # head1, _ = build_ll([1, 4, 7])
    # head2, _ = build_ll([2, 5, 8])
    # head3, _ = build_ll([3, 6, 9])

    # head1, _ = build_ll([1, 2, 3, 23])
    # head2, _ = build_ll([4, 5, 6])
    # head3, _ = build_ll([7, 8])

    head1, _ = build_ll(sorted([random.randint(1, 100) for _ in range(5)]))
    head2, _ = build_ll(sorted([random.randint(1, 100) for _ in range(3)]))
    head3, _ = build_ll(sorted([random.randint(1, 100) for _ in range(4)]))
    head4, _ = build_ll([-5])
    head5, _ = build_ll([999])

    #lists = []
    #lists = [None]
    #lists = [head1]
    #lists = [None, None]
    #lists = [None, head1]
    #lists = [head1, None]
    #lists = [None, head1, None]

    #lists = [head1, head2]
    #lists = [head1, head1] # this will hang due to repeated list
    #lists = [head1, head2, head3]
    lists = [None, head5, head1, None, head2, head3, head4, None]

    print("\nSorted linked lists:")
    for ll in lists:
        print(ll)

    #head, tail = sorted_merge(lists) # min heap; __lt__() defined in Node
    #head, tail = sorted_merge1b(lists) # min heap; don't assume __lt__()...
    head, tail = sorted_merge2(lists) # use array instead of min heap
    #head = sorted_merge_rec(lists) # recursively merge 2 lists at a time
    
    print("\nSorted, merged linked list:")
    print(head)

    #print("\nVerify that it is actually sorted:")
 
"""
dcp131
LC138 (medium)

This question was asked by Snapchat.

Given the head to a singly linked list, where each node also has a “random” pointer that points to anywhere in the linked list, deep clone the list.

"""

import pprint
class Node():
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

    def __repr__(self):
        return f"{self.val}, {self.next.__repr__()}"
        #return f"{self.val}({self.random.val}), {self.next.__repr__()}"

    
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
"""
Solution#1: First clone list by having the random pointers point to their 
corresponding original node.  Store each node in a dict mapping original list 
nodes to their clones.  Then go back and fill in the random pointers for the 
clones by using this dict.

O(n) time, O(n) space.
Doesn't modify original list.
"""

def clone(head):
    if head is None:
        return None

    head_twin = Node(head.val)
    twin = head_twin
    
    twin.random = head # temporarily point to node being cloned
    d = {head: twin}

    while head.next:
        head = head.next
        twin.next = Node(head.val)
        twin = twin.next

        twin.random = head # temporarily point to node being cloned
        d[head] = twin
    
    ### Go back and fill in the correct randmo pointers by using the dict.
    twin = head_twin
    while twin:
        twin.random = d[twin.random.random]
        twin = twin.next

    return head_twin



###############################################################################

"""
Solution#2: first create cloned list by interleaving it into the original list.

O(n) time, O(1) space
"""

def clone2(head):
    if head is None:
        return None

    ### interleave nodes and their clones
    node = head 

    while node:
        temp = node.next
        node.next = Node(node.val)
        node.next.next = temp
        node = node.next.next

    ### copy the random pointers
    node = head
    while node:
        node.next.random = node.random.next # key line
        node = node.next.next

    print(head)

    ### separate the original linked list and its clone
    node = head
    twin = head.next
    twin_head = twin

    while node:
        node.next = node.next.next # twin.next
        
        # need to check since there is only one "None" at end of 
        # interleaved linked list
        if twin.next: 
            twin.next = twin.next.next
        else:
            twin.next = None
        
        node = node.next
        twin = twin.next

    return twin_head


###############################################################################

import random

lst = list(range(1,10))
head, _ = build_ll(lst)

### add nodes to array
nodes = []
node = head
while node:
    nodes.append(node)
    node = node.next

### assign random pointers for each node
node = head
max_randint = len(nodes) - 1
while node:
    node.random = nodes[random.randint(0, max_randint)]
    node = node.next

print("\nhead: ", head)

#head2 = clone(head)
head2 = clone2(head)

print("\nclone: ", head2)

### Modify original linked list and check that cloned list is not modified
node = head
k = 0
while node:
    k -= 1
    node.val = k
    node = node.next

print("\nmodified original: ", head)
print("\ncloned list:", head2)


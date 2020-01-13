"""
dcp104

This problem was asked by Google.

Determine whether a doubly linked list is a palindrome. What if it’s singly linked?

For example, 1 -> 4 -> 3 -> 4 -> 1 returns true while 1 -> 4 returns false.
"""

class Node():
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f"{self.val}, {self.next.__repr__()}"


def build_dll(it):
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
        tail.next.prev = tail # only extra line needed for doubly linked list
        tail = tail.next
        val = next(it, None)

    return head, tail

###############################################################################

"""
For doubly linked list.
O(n) time, O(1) space
"""
def is_palindrome_dll(head, tail=None):
    if (head is None) or (head.next is None):
        return True

    if tail is None:
        tail = head
        while tail and tail.next:
            tail = tail.next

    while (head != tail) and (head.prev != tail):
        if head.val != tail.val:
            return False

        head = head.next
        tail = tail.prev

    return True

###############################################################################

"""
Solution#1 for singly linked list.
Copy values to array and check if array is palindrome.
O(n) time, O(n) space
"""
def is_palindrome(head):
    arr = []

    node = head
    while node:
        arr.append(node.val)
        node = node.next

    for k in range( len(arr)//2 ):
        if arr[k] != arr[len(arr) - k - 1]:
            return False

    return True

"""
Solution#2 for singly linked list.
No array, no reversing any list.
O(n^2) time, O(1) space
"""
def is_palindrome2(head):
    if head is None:
        return True

    # Find middle node (if pair of middle nodes, then take 2nd of pair)
    fast = head
    slow = head
    k = 0

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        k += 1

    #print(f"slow.val = {slow.val}, k = {k}")

    # Advance head one node at a time.
    # Advance slow pointer to node to check against head.

    if fast is None: # even number of nodes
        rng = range(k-1, -1, -1) # k-1, k-2, ..., 0
    else: # odd number of nodes
        rng = range(k, 0, -1) # k, k-1, ..., 1
        
    for i in rng:
        temp = slow
        for _ in range(i):
            temp = temp.next
    
        #print(f"head.val = {head.val}, temp.val = {temp.val}")
        if head.val != temp.val:
            return False

        head = head.next

    return True

"""
For is_palindrome2() - no array, no reversing

Example: (H = head, S = slow, F = fast)
1 2 3 4
H   S   F

k = 2, F = None, n even... check +(k-1), ..., +0
H=1, S+1
H=2, S+0

Example:
1 2 3 4 5
H   S   F

k = 2, F not None, n odd... check +k, ..., +1
H=1, S+2
H=2, S+1

"""


"""
Solution #3 for singly linked list.  
Reverses 2nd half of linked list.
Modifies list, but if wanted, we could restore it to original list
by reversing the 2nd half a second time.
O(n) time, O(1) space
"""
def is_palindrome3(head):
    if head is None:
        return True

    # 1. Find middle node (if pair of middle nodes, then take 2nd of pair)
    fast = head
    slow = head
    
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    
    # 2. Reverse the 2nd half
    prev = None

    while slow:
        temp = slow.next
        slow.next = prev # on 1st iteration, this truncates list given by head
        prev = slow
        slow = temp

    # "prev" is now head of reversed list

    # 3. Compare the 1st half with the reversed 2nd half
    while head and prev:
        if head.val != prev.val:
            return False

        head = head.next
        prev = prev.next

    return True


"""
Solution#4 for singly linked list.  
Reverses 2nd half of linked list.
Modifies list, but restores it to original list before returning
by reversing the 2nd half a second time.
O(n) time, O(1) space
"""

def reverse_list(head):
    prev = None

    while head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    
    return prev # head of reversed list
    
def is_palindrome4(head):
    if head is None:
        return True
    
    # 1. Find middle node (if pair of middle nodes, then take 1st of pair)
    fast = head.next
    slow = head
    
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # slow is now middle of list
    # It will be tail of truncated first half, and be used to restore list.
    
    # 2. Reverse the 2nd half
    rev = reverse_list(slow.next)
    rev2 = rev # used to restore list later
    
    # 3. Compare the 1st half with the reversed 2nd half
    while head and rev:
        if head.val != rev.val:
            slow.next = reverse_list(rev2)
            return False

        head = head.next
        rev = rev.next

    ### Restore original 
    slow.next = reverse_list(rev2)
    
    return True

###############################################################################

if __name__ == "__main__":
    #head, tail = None, None
    #head, tail = build_dll([1])
    #head, tail = build_dll([1, 1])
    #head, tail = build_dll([1, 2])

    #head, tail = build_dll([1, 2, 1])
    #head, tail = build_dll([1, 2, 2, 1])
    #head, tail = build_dll([1, 2, 3, 1])

    #head, tail = build_dll([1, 2, 3, 3, 1])
    #head, tail = build_dll([1, 2, 3, 2, 1])
    head, tail = build_dll([1, 2, 3, 4, 5])

    #head, tail = build_dll([1, 2, 3, 4, 5, 4, 3, 2, 1])
    #head, tail = build_dll([1, 2, 3, 4, 5, 6, 7, 8, 9])

    print(f"\nLinked list:\n{head}")

    p1 = is_palindrome_dll(head) # tail not given, so function finds it
    p2 = is_palindrome_dll(head, tail) # give tail explicitly
    p3 = is_palindrome(head) # singly-linked, use array
    p4 = is_palindrome2(head) # singly-linked, no array, no reversing
    
    print("\nIs palindrome?")
    print(f"\n{p1} - doubly linked, no tail given")
    print(f"\n{p2} - doubly linked, tail given")
    print(f"\n{p3} - singly linked, use array")
    print(f"\n{p4} - singly linked, no array, no reversing")

    p6 = is_palindrome4(head) # singly-linked, reverses 2nd half, restores list
    print(f"\n{p6} - singly linked, reverses 2nd half, restores list")
    print(f"\n-- Check that list is restored: {head}")

    p5 = is_palindrome3(head) # singly-linked, reverses 2nd half
    print(f"\n{p5} - singly linked, reverses 2nd half")
    print(f"\n-- Check that list may be modified: {head}")
    

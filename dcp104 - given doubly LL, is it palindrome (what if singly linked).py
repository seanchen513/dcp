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

# For doubly linked list.
# O(n) time, O(1) space
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


# For singly linked list.
# Copy values to array and check if array is palindrome.
# O(n) time, O(n) space
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


# For singly linked list.
# O(n^2) time, O(1) space
def is_palindrome2(head):
    if head is None:
        return None

    ### Find middle node (if pair of middle nodes, then take 2nd of pair)
    fast = head
    slow = head
    k = 0

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        k += 1

    #print(f"slow.val = {slow.val}, k = {k}")

    ### Advance head one node at a time.
    ### Advance slow pointer to node to check against head.

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

###############################################################################

#head = None
#head, tail = build_dll([1])
#head, tail = build_dll([1, 1])
#head, tail = build_dll([1, 2])

#head, tail = build_dll([1, 2, 1])
#head, tail = build_dll([1, 2, 2, 1])
#head, tail = build_dll([1, 2, 3, 1])

#head, tail = build_dll([1, 2, 3, 3, 1])
head, tail = build_dll([1, 2, 3, 2, 1])


print(f"\n{head}")

p1 = is_palindrome_dll(head) # tail not given, so function finds it
p2 = is_palindrome_dll(head, tail) # give tail explicitly

p3 = is_palindrome(head) # singly-linked, use array
p4 = is_palindrome2(head) # singly-lined, don't use array

print("\nIs palindrome? (doubly linked, no tail given) {}".format(p1))
print("\nIs palindrome? (doubly linked, tail given) {}".format(p2))
print("\nIs palindrome? (singly linked, use array) {}".format(p3))
print("\nIs palindrome? (singly linked, no array) {}".format(p4))


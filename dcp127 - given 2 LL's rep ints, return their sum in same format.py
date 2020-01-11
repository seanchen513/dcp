"""
dcp127

This problem was asked by Microsoft.

Let's represent an integer in a linked list format by having each node represent a digit in the number. The nodes make up the number in reversed order.

For example, the following linked list:

1 -> 2 -> 3 -> 4 -> 5
is the number 54321.

Given two linked lists in this format, return their sum in the same linked list format.

For example, given

9 -> 9
5 -> 2
return 124 (99 + 25) as:

4 -> 2 -> 1
"""


class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}, {self.next.__repr__()}"


def int_to_ll(n):
    head = None
    tail = None

    while n:
        if tail:
            tail.next = Node(n % 10)
            tail = tail.next
        else:
            head = Node(n % 10)
            tail = head

        n //= 10

    return head


def ll_to_int(head):
    n = 0
    p = 1
    
    while head:
        n += head.val * p
        p *= 10
        head = head.next

    return n


###############################################################################

def ll_add(a, b):
    c = None    
    carry = 0

    while a or b or carry:
        val = carry
        if a:
            val += a.val
        if b:
            val += b.val

        if val > 9:
            val -= 10
            carry = 1
        else:
            carry = 0

        if c is None:
            c = Node(val)
            head = c
        else:
            c.next = Node(val)
            c = c.next

        if a:
            a = a.next
        if b:
            b = b.next

    return head

###############################################################################

# a = Node(9, Node(9))
# b = Node(5, Node(2))

a = int_to_ll(99)
b = int_to_ll(25)

c = ll_add(a, b)

print("\na\t= ", a)
print("b\t= ", b)
print("sum\t= ", c)

print("\nConverting from linked lists to integers:")
print("a\t= ", ll_to_int(a))
print("b\t= ", ll_to_int(b))
print("sum\t= ", ll_to_int(c))


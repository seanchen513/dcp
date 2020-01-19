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

"""
LC2. Add Two Numbers
Medium

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}, {self.next.__repr__()}"

def int_to_ll(n):
    head = Node(n % 10)
    tail = head
    n //= 10

    while n:
        tail.next = Node(n % 10)
        tail = tail.next
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
"""
Solution #1: do node by node and use carry, all in one 
Fastest solution here.

O(max(m, n)) time
O(max(m, n)) extra space - length of new list is at most max(m,n) + 1
"""
def ll_add(l1, l2):
    c = None # linked list that we build to be sum of a and b
    carry = 0

    while l1 or l2:
        val = carry
        if l1:
            val += l1.val
        if l2:
            val += l2.val

        if val > 9:
            val -= 10
            carry = 1
        else:
            carry = 0

        ## alternatively:
        #val = val % 10
        #carry = val // 10

        if c is None:
            c = Node(val)
            head = c
        else:
            c.next = Node(val)
            c = c.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    if carry:
        c.next = Node(1)

    return head

###############################################################################
"""
Solution #2: find sum while traversing both linked lists, 
then convert sum to linked list.
"""
def ll_add2(l1, l2):
    num = 0
    p = 1 # power of ten
    
    while l1 and l2:
        num += (l1.val + l2.val) * p
        p *= 10
        l1 = l1.next
        l2 = l2.next
        
    while l1:
        num += l1.val * p
        p *= 10
        l1 = l1.next
        
    while l2:
        num += l2.val * p
        p *= 10
        l2 = l2.next
        
    head = Node(num % 10)
    tail = head
    num //= 10
    
    while num > 0:
        tail.next = Node(num % 10)
        num //= 10
        tail = tail.next
        
    return head

###############################################################################
"""
Solution #3: convert each linked list to integer, add, then convert sum
to linked list.

This is slower than the other 2 solutions.
"""
def ll_add3(l1, l2):
    a = ll_to_int(l1)
    b = ll_to_int(l2)

    return int_to_ll(a + b)
    
###############################################################################

import timeit

if __name__ == "__main__":

    # a, b = Node(9, Node(9)), Node(5, Node(2))
    #a, b = int_to_ll(99), int_to_ll(25)
    #a, b = int_to_ll(0), int_to_ll(0)
    #a, b = int_to_ll(342), int_to_ll(465) # LC example; answer = 807
    #a, b = int_to_ll(999), int_to_ll(1465)
    a, b = int_to_ll(999012), int_to_ll(91465995)

    #c = ll_add(a, b)
    #c = ll_add2(a, b)
    c = ll_add3(a, b)

    print("\na\t= ", a)
    print("b\t= ", b)
    print("sum\t= ", c)

    ### Convert linked lists back to ints

    print("\nConvert linked lists back to ints using ll_to_int()")
    print(f"\na = {ll_to_int(a):10}")
    print(f"b = {ll_to_int(b):10}")
    print(f"c = {ll_to_int(c):10}")

    ###

    t1 = timeit.timeit("c = ll_add(a, b)", "from __main__ import ll_add, a, b", number=10000)
    t2 = timeit.timeit("c = ll_add2(a, b)", "from __main__ import ll_add2, a, b", number=10000)
    t3 = timeit.timeit("c = ll_add3(a, b)", "from __main__ import ll_add3, a, b", number=10000)

    print("\nTimes for ll_add(), ll_add2(), ll_add3():")
    print(f"\nt1  = {t1}")
    print(f"t2  = {t2}")
    print(f"t3  = {t3}")

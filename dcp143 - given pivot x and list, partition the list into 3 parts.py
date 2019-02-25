"""
dcp#143

This problem was asked by Amazon.

Given a pivot x, and a list lst, partition the list into three parts.

The first part contains all elements in lst that are less than x
The second part contains all elements in lst that are equal to x
The third part contains all elements in lst that are larger than x
Ordering within a part can be arbitrary.

For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], one partition may be `[9, 3, 5, 10, 10, 12, 14].
"""


class List():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def print(self):
        if self.val is None:
            print("null ")
        else:
            print(str(self.val) + " ")

        if self.next is not None:
            self.next.print()


def partition(lst, x):
    pass





################################################################################

# using Python lists; stable
def partition2(lst, x):
    p_lt = []
    p_eq = []
    p_gt = []

    for y in lst:
        if y < x:
            p_lt.append(y)
        elif y > x:
            p_gt.append(y)
        else:
            p_eq.append(y)

    return p_lt + p_eq + p_gt # shallow copy

################################################################################

x = 10
lst = [9, 12, 3, 5, 14, 10, 10]

p = partition2(lst, x)

print("x = {}".format(x))
print("list = {}".format(lst))
print("partitioned list = {}".format(p))

################################################################################

# assume lst has at least one element
ll = List(lst[0])
prev = ll

if len(lst) > 0:
    for x in lst[1:]:
        curr = List(x)
        prev.next = curr

print("linked list:")
ll.print()

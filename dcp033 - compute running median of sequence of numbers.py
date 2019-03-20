"""
dcp#33

This problem was asked by Microsoft.

Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2
"""


def insert(a, x):
    n = len(a) - 1
    a.append(x)

    k = 0
    for i in range(n, -1, -1):
        if a[i] > x:
            a[i+1] = a[i]
        else:
            k = i + 1
            break

    a[k] = x


# Solution #1: use insertion sort
def running_median(seq):
    sortd = []
    n = 0

    for x in seq:
        insert(sortd, x)
        print("="*80)
        print("inserting {}".format(x))
        print("after insert, sortd = {}".format(sortd))

        n += 1
        if n % 2 == 0:
            index = n // 2
            median = (sortd[index - 1] + sortd[index]) / 2.0
        else:
            median = sortd[n // 2]

        print("step {}: median {}".format(n, median))



# Solution #2: use heaps



# Solution #3: use self-balancing BST's



seq = [2, 1, 5, 7, 2, 0, 5]
running_median(seq)


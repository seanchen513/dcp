"""
dcp099
same as dcp373, dcp393
LC128 hard

This problem was asked by Microsoft.

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""

"""
dcp393

This problem was asked by Airbnb.

Given an array of integers, return the largest range, inclusive, of integers that are all included in the array.

For example, given the array [9, 6, 1, 3, 8, 10, 12, 11], return (8, 12) since 8, 9, 10, 11, and 12 are all in the array.
"""

# Clarify: can array contain duplicates?  Assume yes.

"""
Solution#1: brute force - try to count from each number in array.
O(n^3) time
O(1) space
"""
def largest_range(arr):
    if (arr is None) or (arr == []):
        return None

    max_start = max_end = arr[0]

    for start in arr:
        x = start

        while x in arr: # O(n) lookup in array
            x += 1

        if (x - 1) - start > max_end - max_start:
            max_start = start
            max_end = x - 1
        
    return (max_start, max_end)


"""
Solution#2: using sorting.
O(n log n) time due to sorting
O(1) space if we can modify the input array.
O(n) space if we need to store a sorted copy (as we do here).
"""
def largest_range2(arr):
    if (arr is None) or (arr == []):
        return None

    a = sorted(arr) # O(n log n)
    # print(f"\nsorted: {a}")

    # indices for range of max length found so far
    max_start = max_end = a[0]
    
    # indices for current sequence of consecutive integers
    start = end = a[0]

    for i in range(1, len(a)):
        if (a[i] == a[i-1]) or (a[i] == a[i-1] + 1): # handles duplicates
            end = a[i]
        else:
            if end - start > max_end - max_start:
                max_start = start
                max_end = end

            start = a[i]
            end = a[i]

        # print("\nbegin = {}, end = {}".format(begin, end))
        # print("max_begin = {}, max_end = {}".format(max_begin, max_end))

    if end - start > max_end - max_start:
        max_start = start
        max_end = end

    return (max_start, max_end)

"""
Solution#3: use set, and only count from numbers that haven't been and
won't be counted up from other numbers.
"""
def largest_range3(arr):
    if (arr is None) or (arr == []):
        return None

    s = set(arr)
    max_start = max_end = arr[0]

    for x in s:
        if x - 1 not in s:
            start = x
            end = x

            while end + 1 in s:
                end += 1

            if end - start > max_end - max_start:
                max_start = start
                max_end = end

    return (max_start, max_end)


###############################################################################

import random
from timeit import default_timer as timer

#arr = [5]
#arr = [5, 4]
#arr = [5, 7]

#arr = [100, 4, 200, 1, 3, 2] # dcp99
#arr = [5, 2, 99, 3, 4, 1, 100] # dcp373
#arr = [9, 6, 1, 3, 8, 10, 12, 11] # dcp393
arr = [9, 6, 0, 2, -2, 1, 3, 8, 10, 12, 11, -1]

arr = [random.randint(1, 1000) for _ in range(1000)]

# print(f"\narray = {arr}")
# print(f"\nsorted(array) = {sorted(arr)}")

start = timer()
r1 = largest_range(arr) # brute force O(n^3)
t1 = timer() - start

start = timer()
r2 = largest_range2(arr) # sort O(n log n)
t2 = timer() - start

start = timer()
r3 = largest_range3(arr) # set O(n)
t3 = timer() - start

print(f"\nlargest range (brute force) = {r1}")
print(f"largest range (sort) = {r2}")
print(f"largest range (set) = {r3}")

print(f"\ntime (brute force) = {t1}")
print(f"time (sort) = {t2}")
print(f"time (set) = {t3}")

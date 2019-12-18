"""
dcp#393

This problem was asked by Airbnb.

Given an array of integers, return the largest range, inclusive, of integers that are all included in the array.

For example, given the array [9, 6, 1, 3, 8, 10, 12, 11], return (8, 12) since 8, 9, 10, 11, and 12 are all in the array.
"""

# O(n log n) because of sorting

def largest_range(arr):
    a = sorted(arr)

    # indices for range of max length found so far
    max_begin = max_end = 0
    
    # indices for current sequence of consecutive integers
    begin = end = 0

    for i in range(1, len(a)):
        if a[i] == a[i-1] + 1:
            end = i
        else:
            begin = end = i
            if end - begin > max_end - max_begin:
                max_begin = begin
                max_end = end

        # print("\nbegin = {}, end = {}".format(begin, end))
        # print("max_begin = {}, max_end = {}".format(max_begin, max_end))

    if end - begin > max_end - max_begin:
        max_begin = begin
        max_end = end

    return (a[max_begin], a[max_end])


arr = [9, 6, 1, 3, 8, 10, 12, 11]

print("array = {}".format(arr))

r = largest_range(arr)
print("\nlargest range = {}".format(r))


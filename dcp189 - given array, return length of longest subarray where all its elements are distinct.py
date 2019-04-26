"""
dcp#189

This problem was asked by Google.

Given an array of elements, return the length of the longest subarray where all its elements are distinct.

For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest subarray of distinct elements is [5, 2, 3, 4, 1].
"""


# Uses sliding window technique.
# O(n) time because inner index "end" only traverses the array once across all outer loops.
# O(n) space because we use a set.
def length_maximal_subarrays(arr):
    n = len(arr)
    s = set() # to keep track of distinct elements

    end = 0 # end of subarray (sliding window)
    max_length = 1

    for start in range(0, n):
        while ((end < n) and (arr[end] not in s)):
            s.add(arr[end])
            end += 1            

        max_length = max(max_length, end - start)

        # We can stop early if "end" reaches the end of the array.
        if end == n:
            break

        # remove first/left element of subarray before "start" is incremented
        s.remove(arr[start])

    return max_length


# Almost same as length_maximal_subarrays() but keeps track of and returns
# maximal subarrays starting at each array element.
# Doesn't stop prematurely if "end" reaches end of array.
def maximal_subarrays(arr):
    n = len(arr)
    s = set() # to keep track of distinct elements

    end = 0 # end of subarray (sliding window)
    subarrays = []

    for start in range(0, n):
        while ((end < n) and (arr[end] not in s)):
            s.add(arr[end])
            end += 1            
         
        subarrays.append(arr[start:end])

        # remove first/left element of subarray before "start" is incremented
        s.remove(arr[start])

    return subarrays


################################################################################
# Essentially the same algorithms as above but with outer loop based on "end".
# Also, no "for" loops so that each end can be moved by more than one position at a time.

def length_maximal_subarrays2(arr):
    n = len(arr)
    s = set() # to keep track of distinct elements

    start = 0 # start of subarray (sliding window)
    end = 0
    max_length = 1

    while end < n:
        while ((end < n) and (arr[end] not in s)):
            s.add(arr[end])
            end += 1            

        # duplicate found at position "end"
        max_length = max(max_length, end - start)

        if end == n:
            break

        # remove elements from left side until subarray contains no duplicates
        while arr[end] in s:
            s.remove(arr[start])
            start += 1

    return max_length


def maximal_subarrays2(arr):
    n = len(arr)
    s = set() # to keep track of distinct elements

    start = 0 # start of subarray (sliding window)
    end = 0
    subarrays = []

    while end < n:
        while ((end < n) and (arr[end] not in s)):
            s.add(arr[end])
            end += 1            

        # duplicate found at position "end"
        subarrays.append(arr[start:end])

        if end == n:
            break

        # remove elements from left side until subarray contains no duplicates
        while arr[end] in s: # note arr[end]
            s.remove(arr[start])
            start += 1

    return subarrays


################################################################################

arr = [1] # max_length = 1
arr = [1, 1, 1, 1, 1] # max_length = 1
arr = [1, 2, 3, 4, 5] # max_length = 5
arr = [5, 2, 3, 5, 4, 3] # max length = 4
#arr = [5, 1, 3, 5, 2, 3, 4, 1] # max length = 5

print("\narray = {}".format(arr))

max_subarrays1 = maximal_subarrays(arr)
max_subarrays2 = maximal_subarrays2(arr)
print("\nmaximal subarrays1 = {}".format(max_subarrays1))
print("\nmaximal subarrays2 = {}".format(max_subarrays2))

max_length1 = length_maximal_subarrays(arr)
max_length2 = length_maximal_subarrays2(arr)
print("\nmax length1 = {}".format(max_length1))
print("\nmax length2 = {}".format(max_length2))


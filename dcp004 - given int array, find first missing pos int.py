"""
dcp#4

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.

"""


# Naive method: search for all positive integers, starting with 1.
# At worst, search n+1 numbers.  This takes O(n^2) worst-case.

# Can use sorting then do linear scan of array.
# This takes O(n log n + n) = O(n log n).

# Can use hashing.  Hash all positive integers in array, then scan hash table
# for first missing positive integer.
# This takes O(n) on average, but requires O(n) extra space.

################################################################################
# Solution with O(n) time, O(1) space.

def first_missing_pos_int(a):
    # segregate positive values to left

    n = len(a)
    j = 0

    for i in range(0, n):
        if a[i] > 0:
            a[i], a[j] = a[j], a[i]
            j += 1

    # j is now count of positive values in "a"
    # We only need to track if values 1, 2, ..., j are in "a"

    # Mark a[i] as present if in range 1..j by making sign of a[a[i] - 1] negative.
    # We use a[i] - 1 as index to offset 1..j to 0..j-1.

    # All numbers in this range should be positive in the original array, 
    # but might been marked negative as part of our algorithm.
    for i in range(0, j): 
        x = abs(a[i]) # abs in case a[i] was previously marked

        if (x >= 1) and (x <= j):
            a[x - 1] = -abs( a[x - 1] ) # abs in case a[x-1] was previously marked

    # The first missing positive integer is the first index i that has positive value a[i].
    for i in range(0, j):
        if a[i] > 0:
            return i + 1

    # worst case: integers 1..j are present, so return j + 1
    return j + 1


################################################################################

a = [3, 5, -1, 1, 4, 2] # 6
a = [1, 2, 0] # 3
a = [3, 4, -1, 1] # 2
a = [2, 3, 7, 6, 8, -1, -10, 15] # 1
a = [2, 3, -7, 6, 8, 1, -10, 15] # 4
a = [1, 1, 0, -1, -2] # 2 ... solution#1 gives incorret answer of 1

a = [-1] # 1
a = [0] # 1

a = [1] # 2
a = [1, 1] # 2
a = [1, 1, 1] # 2
a = [1, 1, 1, 1] # 2
a = [1, 1, 1, 1, 1] # 2

print("array = {}".format(a))

f = first_missing_pos_int(a)

print("modified array = {}".format(a))
print("first missing positive integer = {}".format(f))



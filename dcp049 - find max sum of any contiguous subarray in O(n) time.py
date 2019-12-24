"""
dcp#49
dip#36

This problem was asked by Amazon.

Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.

"""

"""
Some cases:
1. If array elements >= 0, then max sum is sum of entire array.

2. If array elements <= 0, then max sum is 0 (by taking empty subarray).
- If can't take empty subarray, then max sum is the non-positive element
with smallest absolute value.

Note:
- Different subarrays may have the same sum.

"""

# Brute-force solution O(n^2):
# Look at sums of all possible contiguous subarrays.
# Extra: keep track of indices for max subarray.
def max_subarray_sum(arr):
    n = len(arr)
    max_sum = 0

    # extra vars to keep track of indices for max subarray
    start = n # so Python prints empty list [] for subarray[start:end+1] if subarray is empty
    end = 0

    for i in range(n):
        curr_sum = 0

        for j in range(i, n):
            curr_sum += arr[j]

            if curr_sum > max_sum:
                max_sum = curr_sum
                start = i
                end = j

    return max_sum, start, end


# Kadane's algorithm is O(n).
# Idea: keep extending subarray to the right as long as sum is positive.
# If sum turns negative, "reset" the start of the subarray.
# Extra: keep track of indices for max subarray.
def max_subarray_sum2(arr):
    n = len(arr)
    max_so_far = 0
    curr_max = 0

    # extra vars to keep track of indices for max subarray
    start = 0
    end = 0

    for i in range(n):
        curr_max += arr[i]

        if curr_max < 0: # reset start of subarrays we look at
            curr_max = 0
            start = i + 1

        elif curr_max > max_so_far:
            max_so_far = curr_max
            end = i

    return max_so_far, start, end


arr = [34, -50, 42, 14, -5, 86]
#arr = [-5, -1, -8, -9]

# other test cases
# arr = []
# arr = [5]
# arr = [-1]
# arr = [0]

print("\narray = {}".format(arr))

max_sum, start, end = max_subarray_sum(arr)
print("\nBrute force:")
print("max sum = {}".format(max_sum))
print("start, end = {}, {}".format(start, end))
print("contiguous subarray with max sum: {}".format(arr[start:end+1]))

max_sum, start, end = max_subarray_sum2(arr)
print("\nKadane's algorithm:")
print("max sum = {}".format(max_sum))
print("start, end = {}, {}".format(start, end))
print("contiguous subarray with max sum: {}".format(arr[start:end+1]))


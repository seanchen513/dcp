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

"""
53. Maximum Subarray
Easy

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

*** NOTE: LC considers max sum of [-1] to be -1, not 0.
"""

###############################################################################
"""
Solution #1: brute force

Look at sums of all possible contiguous subarrays.
Extra: keep track of indices for max subarray.

O(n^2) time
"""
def max_subarray_sum(arr):
    #max_sum = -float('inf') # if can't take empty subarrays
    max_sum = 0 # if can take empty subarrays

    n = len(arr)

    # Extra vars to keep track of indices for max subarray.
    # start = n so Python prints empty list [] for subarray[start:end+1] 
    # if subarray is empty.
    start = n
    end = 0

    for i in range(n):
        curr_sum = 0

        for j in range(i, n):
            curr_sum += arr[j]

            if curr_sum > max_sum:
                max_sum = curr_sum
                start, end = i, j

    return max_sum, start, end

###############################################################################
"""
Solution #2: Kadane's algorithm

Idea: keep extending subarray to the right as long as sum is positive.
If sum turns negative, "reset" the start of the subarray.

Extra: keep track of indices for max subarray.

O(n) time
"""
def max_subarray_sum2(arr):
    #max_sum = -float('inf') # if can't take empty subarrays
    max_sum = 0 # if can take empty subarrays
    curr_sum = 0

    # extra vars to keep track of indices for max subarray
    start = 0
    end = 0
    
    n = len(arr)
    
    for i in range(n):
        curr_sum += arr[i]

        if curr_sum < 0: # reset start of subarrays we look at
            curr_sum = 0
            start = i + 1

        elif curr_sum > max_sum:
            max_sum = curr_sum
            end = i

    return max_sum, start, end

###############################################################################
"""
Solution #3: Kadane's algo, in-place

This is for LC53.  Returns only the max sum, not the indices of the max
subarray.  Doesn't take empty subarrays, so returns -1 for [-1].

https://leetcode.com/problems/maximum-subarray/discuss/20396/Easy-Python-Way
"""
def max_subarray_sum3(arr):
    for i in range(1, len(arr)):
        if arr[i-1] > 0:
            arr[i] += arr[i-1]
        
    return max(arr) if arr else 0

def max_subarray_sum3b(arr):
    for i in range(1, len(arr)):
        arr[i] = max(arr[i], arr[i-1] + arr[i])

    return max(arr) if arr else 0

from itertools import accumulate

def max_subarray_sum3c(arr):
    return max(accumulate(arr, lambda x, y: x+y if x > 0 else y)) if arr else 0

###############################################################################
"""
Solution #4: greedy algo.  Calculate running sums from start.  Find largest
difference in running sums.

O(n) time

https://leetcode.com/problems/maximum-subarray/discuss/20200/Share-my-solutions-both-greedy-and-divide-and-conquer
"""
def max_subarray_sum4(arr):
    max_diff = -float('inf') # if can't take empty subarrays
    #max_diff = 0 # if can take empty subarrays

    min = 0
    sum = 0

    for x in arr:
        sum += x

        if sum - min > max_diff:
            max_diff = sum - min

        if sum < min:
            min = sum

    return max_diff

###############################################################################
"""
Solution #5: divide & conquer

m = sum of subarray with largest sum
l = sum of subarray with largest sum starting from first element
r = sum of subarray with largest sum ending at last element
s = sum of whole array

Doesn't take empty sets.  Returns -1 for when input is [-1].
Returns 0 when input is empty array [].
"""
def max_subarray_sum5(arr):
    def dnc(arr, left, right):
        if not arr or left > right:
            return 0, 0, 0, 0
        
        if left == right:
            return arr[left], arr[left], arr[left], arr[left]

        mid = (left + right) // 2

        left_m, left_l, left_r, left_s = dnc(arr, left, mid)
        right_m, right_l, right_r, right_s = dnc(arr, mid+1, right)

        # max subarray is (1) within left subarray, 
        # (2)within right subarray, or (3) some right part of left subarray 
        # plus some left part of right subarray
        m = max(left_m, right_m, left_r + right_l)

        # largest left sum is within left subarray, or entire left subarray
        # plus some left part of right subarray
        l = max(left_l, left_s + right_l)

        # largest right sum is within right subarray, or entire right subarray
        # plus some right part of left subarray
        r = max(right_r, right_s + left_r)

        s = left_s + right_s

        return m, l, r, s

    return dnc(arr, 0, len(arr)-1)[0]

###############################################################################

if __name__ == "__main__":    
    def compare(arr):
        print(f"\narray = {arr}")

        max_sum, start, end = max_subarray_sum(arr)
        
        print("\nBrute force:")
        print(f"max sum = {max_sum}")
        print(f"start, end = {start}, {end}")
        print(f"contiguous subarray with max sum: {arr[start:end+1]}")

        max_sum, start, end = max_subarray_sum2(arr)
        
        print("\nKadane's algorithm:")
        print(f"max sum = {max_sum}")
        print(f"start, end = {start}, {end}")
        print(f"contiguous subarray with max sum: {arr[start:end+1]}")

    def test(arr):
        print(f"\n{arr}")
        
        #max_sum, start, end = max_subarray_sum(arr) # brute force
        #max_sum, start, end = max_subarray_sum2(arr) # Kadane's algo
        #max_sum = max_subarray_sum3(arr)
        #max_sum = max_subarray_sum3b(arr)
        #max_sum = max_subarray_sum3c(arr)
        #max_sum = max_subarray_sum4(arr)
        max_sum = max_subarray_sum5(arr)

        print(f"max sum = {max_sum}")
        #print(f"start, end = {start}, {end}")
        #print(f"contiguous subarray with max sum: {arr[start:end+1]}")

    arr = [-2,1,-3,4,-1,2,1,-5,4] # LC53 example, answer = 6 for [4,-1,2,1]
    #compare(arr)
    #test(arr)

    ###
    arrays = [
        [],
        [5],
        [-1], # answer = 0 if take empty subarray; LC answer is -1
        [0],

        [-5, -1, -8, -9],
        [34, -50, 42, 14, -5, 86],

        [-2,1,-3,4,-1,2,1,-5,4], # LC53 example, answer = 6 for [4,-1,2,1]
    ]
    
    for arr in arrays:
        test(arr)

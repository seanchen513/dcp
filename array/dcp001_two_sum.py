"""
dcp#1

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

"""
LC1. Two Sum
Easy

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

### Assume distinct integers chosen from list.
### Assume list contains only integers and at least 2 integers.

################################################################################
"""
Solution #1: brute force, no sorting

O(n^2) time
"""
def sums_to(arr, target_sum):
    n = len(arr)

    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target_sum:
                return arr[i]
    
    return None

"""
Solution #1b: Same as sol #1, but return indices.
"""
def sums_to1b(arr, target_sum):
    n = len(arr)

    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target_sum:
                return [i, j]
    
    return None

################################################################################
"""
Solution #2: Sort, then use decreasing window ends (bookends).

One pass.
O(n log n) time due to sorting
O(1) extra space
"""
def sums_to2(arr, target_sum):
    #arr.sort()
    arr = sorted(arr)

    left = 0
    right = len(arr) - 1

    while left < right:
        sum = arr[left] + arr[right]

        if sum < target_sum:
            left += 1
        elif sum > target_sum:
            right -= 1
        else:
            return arr[left]

    return None

"""
Solution #2b: Same as sol #2, but return indices.

One pass.
O(n log n) time due to sorting
O(n) extra space
"""
def sums_to2b(arr, target_sum):
    # store original indices before sorting
    a = [(arr[i], i) for i in range(len(arr))]

    a.sort()
    #a = sorted(arr)

    left = 0
    right = len(arr) - 1

    while left < right:
        sum = a[left][0] + a[right][0]

        if sum < target_sum:
            left += 1
        elif sum > target_sum:
            right -= 1
        else:
            return sorted([a[left][1], a[right][1]])

    return None

################################################################################
"""
Solution #3: Use set. (No sorting.)

O(n) since one pass and set (hashmap) operations (here, lookup and insert)
are O(1) amortized on average.
Note: hashmap operations are O(n) worst case if hash buckets are linear,
or O(log n) if hash buckets are self-balancing binary search trees.
"""
def sums_to3(arr, target_sum):
    s = set()

    for k in arr:
        if k in s:
            return k
        else:
            s.add(target_sum - k)

    return None

"""
Solution #3b

Same as sol #3, but use dict instead of set in order to return indices.
"""
def sums_to3b(arr, target_sum):
    d = {}

    for i in range(len(arr)):
        if arr[i] in d:
            return [d[arr[i]], i]
        else:
            d[target_sum - arr[i]] = i

    return None

################################################################################

if __name__ == "__main__":
    arr = [10, 15, 3, 7]
    target_sum = 17

    s1 = sums_to(arr, target_sum)
    s2 = sums_to2(arr, target_sum)
    s3 = sums_to3(arr, target_sum)
    
    s1b = sums_to1b(arr, target_sum)
    s2b = sums_to2b(arr, target_sum)
    s3b = sums_to3b(arr, target_sum)

    print("\nlist = {}".format(arr))
    print("target sum = {}".format(target_sum))

    print(f"\nindices (sol #1b) = {s1b}")
    print(f"indices (sol #2b) = {s2b}")
    print(f"indices (sol #3b) = {s3b}")

    print(f"\nvalues (sol #1)  = {s1}, {target_sum - s1}")
    print(f"values (sol #3)  = {s3}, {target_sum - s2}")
    print(f"values (sol #3)  = {s3}, {target_sum - s2}")
    

"""
dcp#374

This problem was asked by Amazon.

Given a sorted array arr of distinct integers, return the lowest index i for which arr[i] == i. Return null if there is no such index.

For example, given the array [-5, -3, 2, 3], return 2 since arr[2] == 2. Even though arr[3] == 3, we return 2 since it's the lowest index.

"""

# key words: sorted, distinct, integers, lowest
# idea: modified binary search
# O(log n)

def first_fixed_point(arr, low, high):
    if low > high:
        return None

    mid = (low + high) // 2
    if arr[mid] == mid:
        return mid
    elif arr[mid] < mid:
        return first_fixed_point(arr, mid + 1, high)
    else: # arr[mid] > mid
        return first_fixed_point(arr, low, mid - 1)


arr = [-5, -3, 2, 3]

i = first_fixed_point(arr, 0, len(arr))

print("array = {}".format(arr))
print("first fixed point = {}".format(i))


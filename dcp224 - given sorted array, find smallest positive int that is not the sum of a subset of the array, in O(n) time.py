"""
dcp#224

This problem was asked by Amazon.

Given a sorted array, find the smallest positive integer that is not the sum of a subset of the array.

For example, for the input [1, 2, 3, 10], you should return 7.

Do this in O(N) time.
"""

"""
Not used in solutions:
1 =     0001
2 =     0010
3 =     0011
10 =    1010

7 =     0111
"""

# Naive solution: Look at all subsets of array and find their sums.
# Store sums in sorted list.  Then loop through list to find smallest pos int.

# Solution#2: 
# 
# O(n)
def smallest_not_sum(arr):
    smallest_nonsum = 1

    for i in range(0, len(arr)):
        if arr[i] > smallest_nonsum:
            break

        smallest_nonsum += arr[i]

    return smallest_nonsum


arr = [1, 3, 6, 10, 11, 15] # 2
arr = [1, 1, 1, 1] # 5
arr = [1] # 2
arr = [2] # 1
arr = [1, 2, 3, 4, 5, 6] # 22 = 6*7/2 + 1
arr = [1, 2, 3, 10] # from problem statement; should return 7

print("\narray = {}".format(arr))

n = smallest_not_sum(arr)
print("\nsmallest pos int not sum of subset of array = {}".format(n))


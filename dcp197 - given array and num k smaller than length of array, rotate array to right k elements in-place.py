"""
dcp #197

This problem was asked by Amazon.

Given an array and a number k that's smaller than the length of the array, rotate the array to the right k elements in-place.
"""

import math

# Rotate to right by k elements.
# Partition array into gcd(n, k) cycles.
# Rotate elements within each cycle by 1 position within the cycle.
# There length of each cycle is n/gcd(n,k).
# O(n) time
# O(1) space
def rotate(arr, k):
    n = len(arr)
    gcd = math.gcd(n, k)
    num_cycles = int(n / gcd)
    
    print("n = {}".format(n))
    print("k = {}".format(k))
    print("gcd = {}".format(gcd))

    for i in range(0, gcd): # for first element of each cycle...
        temp = arr[i]

        for j in range(0, num_cycles - 1): # for each element in the cycle except last
            prev = (i - k) % n # going backwards
            arr[i] = arr[prev]
            i = prev

        arr[i] = temp



arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
k = 3
# try all test cases: 0, 1, 2, 3, ... 11
# important test cases: 0, 1, > 1 but gcd = 1, gcd > 1
# also works for negative k, and k >= len(arr)

print("array = {}".format(arr))

rotate(arr, k)
print("rotated array = {}".format(arr))


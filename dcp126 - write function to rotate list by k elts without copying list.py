"""
dcp#126

This problem was asked by Facebook.

Write a function that rotates a list by k elements. For example, [1, 2, 3, 4, 5, 6] rotated by two becomes [3, 4, 5, 6, 1, 2]. Try solving this without creating a copy of the list. How many swap or move operations do you need?

"""

# Solution #1: use temp array
# O(n) time
# O(k) aux space
def rotate(a, k):
    # rotate by k elements, so temp will have k elements
    temp = []
    for i in range(0, k):
        temp.append(a[i])

    # shift rest of array over by k positions
    for i in range(k, len(a)):
        a[i-k] = a[i]

    # copy back temp
    for i in range(0, k):
        a[len(a)-k+i] = temp[i]


# same as above but using Python slice notation only
def rotate_python(a, k):
    temp = a[:k]

    # shift rest of array over
    a[:len(a)-k] = a[k:]

    # copy back temp
    a[len(a)-k:] = temp


################################################################################

# for left-rotation by 1 element, use n copy operations and a temp variable
def rotate_left(a):
    temp = a[0]
    n = len(a)

    for i in range(0, n-1):
        a[i] = a[i+1]

    a[n-1] = temp

# Solution #2: repeatedly use rotation by one-element
# O(n*k) time - total n*k copy operations
# O(1) space
def rotate2(a, k):
    for _ in range(0, k):
        rotate_left(a)

################################################################################

"""
Example:
n = 6, k = 4
gcd = 2 (# sets)
size of each set = n/gcd = 3

1 2 3 4 5 6

set 1: 1 5 3
set 2: 2 6 4
"""

import math

# Solution #3: partition array into gcd(n,k) cycles,
# where elements within each cycle are shifted by "one" position within the cycle.
# The length of each cycle is n/gcd(n,k).
# O(n) time
# O(1) space
def rotate3(a, k):
    n = len(a)
    gcd = math.gcd(n, k) # sets
    set_size = int(n / gcd)

    print("n = {}".format(n))
    print("k = {}".format(k))
    print("gcd = {}".format(gcd))

    for i in range(0, gcd): # first element of each set
        temp = a[i]
        index = i
        for j in range (0, set_size - 1):
            next_index = (index + k) % n
            a[index] = a[next_index] 
            index = next_index

        a[index] = temp

################################################################################

"""
Example:
n = 6
k = 2

123456
345612

swap 1,3
321456

swap 2,4
341256

swap 1,5
345216

swap 2,6
345612

4 swaps
"""

# Solution #4: use swaps
# unfinished
def rotate4(a, k):
    for i in range(k, len(a)):
        a[i], a[i-k] = a[i-k], a[i]
                
    # still need to adjust end of array

################################################################################

a = [1, 2, 3, 4, 5, 6]
k = 2

print("list =\n{}".format(a))
print("rotate left by {} elements".format(k))

print("\nlist after rotation:")

print("\nSolution #1")
b = a.copy()
rotate(b, k)
print(b)

print("\nSolution #1 (Python slicing):")
b = a.copy()
rotate_python(b, k)
print(b)

print("\nSolution #2:")
b = a.copy()
rotate2(b, k)
print(b)

print("\nSolution #3:")
b = a.copy()
rotate3(b, k)
print(b)


"""
dcp#155

This problem was asked by MongoDB.

Given a list of elements, find the majority element, which appears more than half the time (> floor(len(lst) / 2.0)).

You can assume that such element exists.

For example, given [1, 2, 1, 1, 3, 4, 0], return 1. [sic: bad example]
"""

"""
169. Majority Element
Easy

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""

###############################################################################
"""
Solution #1: brute force, double nested loops to count.

Alternatively, could have inner loop go over all elements in array,
and have count start at 0 in outer loop.

O(n^2) time
O(1) extra space
"""
def majority_elt(arr):
    n = len(arr)

    if n == 1: # inner loop isn't entered
        return arr[0]

    threshold = n // 2

    for i in range(n):
        count = 1
        x = arr[i]

        for j in range(i+1, n):
            if arr[j] == x:
                count += 1
            
                if count > threshold:
                    return x

###############################################################################
"""
Solution #2: sorting

O(n log n) time due to sorting
O(1) extra space if sort in place, else O(n)
"""
def majority_elt2(arr):
    #if not arr:
    #    return None

    a = sorted(arr)

    return a[len(a)//2]

###############################################################################
"""
Solution #3: count elements and store in dict.
Return key with max value (count).  Double pass.

O(n) time
O(n) extra space for dict
"""
def majority_elt3(arr):
    #if not arr:
    #    return None

    count = {}

    for x in arr:
        count[x] = count.get(x, 0) + 1

    # count = collections.Counter(arr)

    # return key with max value
    return max(count, key=count.get)
    #return max(count, key=lambda k: count[k])

"""
Solution #3b: count elements and store in dict, but return ASAP.  Single pass.
"""
def majority_elt3b(arr):
    threshold = len(arr) // 2
    count = {}

    for x in arr:
        count[x] = count.get(x, 0) + 1

        if count[x] > threshold:
            return x

###############################################################################
"""
Solution #4: use Boyer-Moore majority vote algorithm

O(n) time
O(1) extra space

No need to validate that element found by algo is indeed a majority element
due to assumption of problem statement.
"""
def majority_elt4(arr):
    count = 0
    maj = None

    for x in arr:
        if count == 0:
            maj, count = x, 1
        elif x == maj:
            count += 1
        else:
            count -= 1

    return maj

    # if need to check
    #return maj if arr.count(maj) > len(arr)//2 else None

# index-based version
def majority_elt4b(arr):
    n = len(arr)
    maj_index = 0
    count = 1

    for i in range(n):
        if arr[i] == arr[maj_index]:
            count += 1
        else:
            count -= 1
        
        if count == 0:
            maj_index = i
            count = 1

    return arr[maj_index]

###############################################################################
"""
Solution #5: Randomization

O(\infty) time
O(n) expected time
O(1) extra space
"""
import random

def majority_elt5(arr):
    threshold = len(arr) // 2

    while True:
        candidate = random.choice(arr)

        count = 0
        for x in arr:
            if x == candidate:
                count += 1

        if count > threshold:
            return candidate

        #if sum(1 for x in arr if x == candidate) > threshold:

###############################################################################
"""
Solution #6: divide and conquer, pass indices
"""
def majority_elt6(arr):
    def maj(low, high):
        if low == high:
            return arr[low]

        mid = (low + high) // 2

        left_maj = maj(low, mid)
        right_maj = maj(mid+1, high)

        if left_maj == right_maj:
            return left_maj

        left_count = sum(1 for i in range(low, mid) if arr[i] == left_maj)
        right_count = sum(1 for i in range(mid+1, high) if arr[i] == right_maj)

        return left_maj if left_count > right_count else right_maj

    return maj(0, len(arr) - 1)

"""
Solution #6: divide and conquer, pass (sub)arrays

https://leetcode.com/problems/majority-element/discuss/51712/Python-different-solutions-(dictionary-bit-manipulation-sorting-divide-and-conquer-brute-force-etc).
"""
def majority_elt6b(arr):
    if len(arr) == 1:
        return arr[0]

    mid = len(arr) // 2
    left = majority_elt6b(arr[:mid])
    right = majority_elt6b(arr[mid:])

    if left == right:
        return left

    ### doesn't work for case [2,2,1,1,1,2,2]; gives 1 instead of 2
    #return [right, left][arr.count(right) > mid]

    left_count = sum(1 for x in arr if x == left)
    right_count = sum(1 for x in arr if x == right)

    return left if left_count > right_count else right

###############################################################################
"""
Solution #7: use bit manipulation

Assume given array contains only 32-bit integers.
Count set bits in each bit position over all integers in given array.
Use the bits with count > threshold to form the majority integer.

O(n) time
O(1) extra space

https://leetcode.com/problems/majority-element/discuss/51712/Python-different-solutions-(dictionary-bit-manipulation-sorting-divide-and-conquer-brute-force-etc).
"""
def majority_elt7(arr):
    ### 1. Count the set bits
    bit = [0]*32

    for x in arr:
        for j in range(32):
            bit[j] += (x >> j) & 1

    ### 2. Use bits with count > threshold to form the integer answer.
    maj = 0
    threshold = len(arr) // 2

    for i, val in enumerate(bit):
        if val > threshold:
            # If the 31st bit is 1, then answer is a negative integer.
            # In 2's complement representation, there are leading 1s.
            # Force Python to interpret it as a negative integer
            # rather than as a very big positive integer.
            # Do this by taking the 2's complement (to get the positive
            # version of the integer) and attaching a negative sign.
            if i == 31:
                maj = -((1 << 31) - maj) 
                # maj = -(~maj + 1) # this also works
            else:
                maj |= (1 << i)

    return maj

###############################################################################
"""
Solution #8: use self-balancing binary search tree

O(n^2) time for regular BST; O(n log n) for self-balancing BST
O(n) extra space
"""
def majority_elt8(arr):
    b = bst() # NOT IMPLEMENTED HERE
    threshold = len(arr) // 2

    for x in arr:
        node = b.find(x)

        if node is None:
            node = b.insert(x)
            node.count = 1
        else:
            node.count += 1
        
        if node.count > threshold:
            return node.val
                
###############################################################################

if __name__ == "__main__":
    def test(arr):
        print(f"\n{arr}")

        maj = majority_elt(arr)
        maj2 = majority_elt2(arr)
        maj3 = majority_elt3(arr)
        maj3b = majority_elt3b(arr)
        maj4 = majority_elt4(arr)
        maj4b = majority_elt4b(arr)
        maj5 = majority_elt5(arr)
        maj6 = majority_elt6(arr)
        maj6b = majority_elt6b(arr)
        maj7 = majority_elt7(arr)

        print(f"majority element (sol #1)  = {maj}")
        print(f"majority element (sol #2)  = {maj2}")
        print(f"majority element (sol #3)  = {maj3}")
        print(f"majority element (sol #3b) = {maj3b}")
        print(f"majority element (sol #4)  = {maj4}")
        print(f"majority element (sol #4b) = {maj4b}")
        print(f"majority element (sol #5)  = {maj5}")
        print(f"majority element (sol #6)  = {maj6}")
        print(f"majority element (sol #6b) = {maj6b}")
        print(f"majority element (sol #7)  = {maj7}")

    #arr = []
    #test(arr)

    arr = [5]
    test(arr)

    arr = [3,2,3] # LC ex1; answer = 3
    test(arr)

    arr = [2,2,1,1,1,2,2] # LC ex2; answer = 2
    test(arr)    

    arr = [1, 2, 1, 1, 3, 4, 1] # answer = 1; 1 appears 4 out of 7 times
    test(arr)

    arr = [-2,-2,-1,-1,-1,-2,-2] # test negative integers
    test(arr)

    arr = [0,0,0,1,-1]
    test(arr)

    arr = [-1,1,-1,1,-1,1,-1]
    test(arr)

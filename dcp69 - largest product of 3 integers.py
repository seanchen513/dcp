'''
dcp#69

This problem was asked by Facebook.

Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.
'''

# Idea: two negative integers might be used to form product,
# so need to keep track of largest 2 negatives by magnitude.
# Also need to keep track of largest 3 positives.

# special case: what if at least one 0 in array and 0 is largest product?
# Must mean there is at most one negative, and at most 2 positive.

# WITH SORTING.
# Assume a is array of integers with at least 3 integers (if not, return -1).
# O(n log n) time, O(1) space
def find_largest_product(a):
    n = len(a) - 1 # last index
    if n < 3:
        return -1

    a.sort()

    p1 = a[n-2]*a[n-1]*a[n]
    
    #if a[1] < 0: # there are at least 2 negative numbers
    #    p2 = a[0]*a[1]*a[n]
    #    return max(p1, p2)
    #
    #return p1

    p2 = a[0]*a[1]*a[n]
    return max(p1, p2)

a = [-10, -10, 5, 2] # orig; answer = 500
a = [2, 3, 4] # 24
a = [-2, -3, -4]  # -24
a = [-2, 3, 4] # -24
a = [-4, 0, 2] # 0

a = [-4, -3, -2, -1, 0] # 0
a = [-100, 0, 1, 2] # 0
a = [-100, 0, 1, 2, 3] # 6

p = find_largest_product(a)

print("largest product = {}".format(p))





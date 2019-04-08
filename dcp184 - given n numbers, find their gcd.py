"""
dcp#184

This problem was asked by Amazon.

Given n numbers, find the greatest common denominator between them.

For example, given the numbers [42, 56, 14], return 14.
"""


def gcd(x, y):
    while y != 0:
        x, y = y, x % y

    return x


# Assume nums is nonempty list of integers.
def gcd_list(nums):
    g = nums[0]

    for i in range(1, len(nums)):
        g = gcd(g, nums[i])

    return g


nums = [84] # gcd = 84 
nums = [21, 21, 21, 21, 21] # gcd = 21
nums = [42, 56, 14] # gcd = 14

g = gcd_list(nums)

print("Integers: {}".format(nums))
print("\ngcd: {}".format(g))


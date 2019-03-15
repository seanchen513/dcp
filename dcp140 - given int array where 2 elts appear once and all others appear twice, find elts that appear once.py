"""
dcp#140

This problem was asked by Facebook.

Given an array of integers in which two elements appear exactly once and all other elements appear exactly twice, find the two elements that appear only once.

For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. The order does not matter.

Follow-up: Can you do this in linear time and constant space?

"""


# Solution #1: sort
# O(n log n)
def find_unique_elts(a):
    a.sort()

    unique1 = None
    skips = 0

    for i in range(0, len(a) - 1): # index of 2nd to last element is len(a) - 1
        i += skips
        #print("i = {}".format(i))

        if a[i] != a[i+1]:
            if unique1 is None:
                unique1 = a[i]
            else:
                return unique1, a[i]
        else:
            # i += 1 # doesn't work as expected
            skips += 1



# Solution #2: take XOR of all elements
# Bits from elts that appear twice will cancel out.
# Left with bits set from the two unique elements.
# O(n) time, O(1) space
def find_unique_elts2(a):
    all_xor = a[0]

    for i in range(1, len(a)):
        all_xor ^= a[i]

    # all_xor now only have bits set from the two unique elements.
    # all_xor cannot be 0 since the two unique elements are different from each other.
    # Take one of these set bits.  This bit is set in exactly one of the unique elements.
    # Partition the original array of elements according to whether this bit is set.
    # Each partition contains exactly one of the unique elements.
    # In each partition, the other elements appear exactly twice within that parititon.
    # Within each partition, do XOR of all elements.  
    # This produces the unique element in each partition.

    special_bit = all_xor & ~(all_xor - 1) # get rightmost bit
    #special_bit = all_xor & -all_xor # get rightmost bit
    print("special_bit = {}".format(special_bit))
    xor1 = None
    xor2 = None

    for x in a:
        if x & special_bit:
            if xor1 is None:
                xor1 = x
            else:
                xor1 ^= x
        else:
            if xor2 is None:
                xor2 = x
            else:
                xor2 ^= x

    return xor1, xor2

################################################################################

a = [2, 4, 6, 8, 10, 2, 6, 10]
b = a[:]

print("\na = {}".format(a))

x, y = find_unique_elts(a)

print("unique elements are: {}, {}".format(x, y))

###

print("\nb = {}".format(b))

x, y = find_unique_elts2(b)

print("unique elements are: {}, {}".format(x, y))

# 4 = 0100
# 8 = 1000
# 4 ^ 8 = 11000 = 12
# print("4 ^ 8 = {}".format(4 ^ 8))


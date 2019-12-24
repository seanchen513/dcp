"""
dcp#331

This problem was asked by LinkedIn.

You are given a string consisting of the letters x and y, such as xyxxxyxyy. In addition, you have an operation called flip, which changes a single x to y or vice versa.

Determine how many times you would need to apply this operation to ensure that all x's come before all y's. In the preceding example, it suffices to flip the second and sixth characters, so you should return 2.

"""

# Solution #1:
# Assume string "s" contains only x's and y's.
# O(n) time, O(n) space
def flips_needed(s):
    n = len(s)
    y = [0]*n # count of y's from start of str to current index
    x = [0]*n # count of x's from end of str to current index (going backwards)
    
    if s[0] == 'y':
        y[0] = 1 

    if s[n-1] == 'x':
        x[n-1] = 1 

    for i in range(1, n):
        if s[i] == 'y':
            y[i] = y[i-1] + 1
        else:
            y[i] = y[i-1]

    for i in range(n-2, -1, -1):
        if s[i] == 'x':
            x[i] = x[i+1] + 1
        else:
            x[i] = x[i+1]

    print("y = {}".format(y))
    print("x = {}".format(x))

    # x[0] represents flipping all x's
    # y[n-1] represents flipping all y's
    min_sum = min(x[0], y[n-1])
    flips = [0] * (n+1) # for printing purposes only
    flips[0] = x[0]
    flips[n] = y[n-1]

    for i in range(n-1):
        # y[i] + x[i+1] represents flipping all y's up to and including index i
        # and flipping all x's after index i
        
        flips[i+1] = y[i] + x[i+1]
        min_sum = min(y[i] + x[i+1], min_sum)
    
    print("flips pivoting at index i: {}".format(flips))

    return min_sum


# Solution #2: use bit manipulation
# Assume string "s" contains only x's and y's.
# Longer than O(n) time due to counting bits in key step.
# O(n) space due to bit masks (and conversion of string to bits).
def flips_needed2(s):
    b = str_to_bits(s)
    print("b = {}".format(b))
    n = len(s)

    # All x's come before all y's; ie, all 0's come before all 1's
    # masks: 00..00, 00..01, 00..011, 00..0111, 011..11, 11..11
    # These are 2^k - 1 for k = 0, 1, 2, ..., n

    mask = 0
    min_flips = n
    print("mask, flips")

    for _ in range(n+1):
        flips = bin(b ^ mask).count('1') # key step
        print(mask, flips)
        min_flips = min(flips, min_flips)
        mask = (mask << 1) + 1

    print()
    return min_flips


# For use in solution #2.
# Assume s is string of only x's and y's
# x to 0, and y to 1
# Example: "xyxxxyxyy" converts to 139
def str_to_bits(s):
    b = 0
    n = len(s)
    
    for i in range(n):
        b <<= 1
        if s[i] == 'y':
            b += 1

    return b


###############################################################################

s = "xyxxxyxyy"
#s = "xxxxxxxxx"
#s = "yyyyyyyyy"
print("\nstring = {}".format(s))

print("\n*** Solution using arrays:\n")
n = flips_needed(s)
print("\nmin flips needed = {}".format(n))

print("\n*** Solution using bit manipulation:\n")
n = flips_needed2(s)
print("\nmin flips needed = {}".format(n))


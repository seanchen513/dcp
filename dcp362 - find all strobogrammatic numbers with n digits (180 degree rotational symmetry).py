"""
dcp#362, dcp#402

This problem was asked by Twitter.

A strobogrammatic number is a positive number that appears the same after being rotated 180 degrees. For example, 16891 is strobogrammatic.

Create a program that finds all strobogrammatic numbers with N digits.
"""

"""
digit - rotated 180 degrees
1 - 1
2
3
4
5
6 - 9
7
8 - 8
9 - 6
0 - 0

So the only possible digits are 1, 6, 8, 9, 0.
If there is a middle digit, it must be 1, 8, or 0.
The first and last digits cannot be zero, unless the (entire) number is 0.

num_digits = 1: 3 strobogrammatic numbers

Let n = number of digits.

num_digits even > 1: n/2 slots
- 1st slot has 4 choices (1, 6, 8, 9)
- other n/2 - 1 slots each have 5 choices (1, 6, 8, 9, 0)
- no middle digit
- total number of choices = 4 * 5^(n/2 - 1)

num_digits odd > 1: (n - 1)/2 slots
- 1st slot has 4 choices (1, 6, 8, 9)
- other (n-1)/2 - 1 = (n-3)/2 slots each have 5 choices (1, 6, 8, 9, 0)
- 3 choices for middle digit
- total number of choices = 3 * 4 * 5^[(n-3)/2]

1 - 3
2 - 4
3 - 3*4 = 12
4 - 4 * 5 = 20
5 - 3*4 * 5 = 60
6 - 4 * 5^2 = 100
7 - 3*4 * 5^2 = 300
8 - 4 * 5^3 = 500
9 - 3*4 * 5^3 = 1500
10 - 4 * 5^4 = 2500
"""

# Assume num_digits is positive integer.
def strobo_str(num_digits, depth=1):
    if num_digits == 0:
        return ['']

    if num_digits == 1:
        return ['0', '1', '8']
    
    lst = strobo_str(num_digits - 2, depth + 1)
    nums = []

    for base in lst:
        nums += ['1' + base + '1',
            '6' + base + '9',
            '8' + base + '8',
            '9' + base + '6']

        if depth > 1:
            nums.append('0' + base + '0')
        
    return nums


def strobo(num_digits):
    lst = strobo_str(num_digits)
    nums = [int(s) for s in lst]

    return sorted(nums)


###############################################################################

num_digits = 3

s = strobo(num_digits)

print("\nstrobogrammatic numbers with {} digits:\n{}".format(num_digits, s))
print("\nnumber of strobogrammatic numbers with {} digits = {}".format(num_digits, len(s)))

print("\n# digits - # of strobogrammatic numbers with # digits")

for num_digits in range(1, 16):
    print("{} - {}".format(num_digits, len(strobo(num_digits))))


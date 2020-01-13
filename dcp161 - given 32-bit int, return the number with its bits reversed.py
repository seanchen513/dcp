"""
dcp#161

This problem was asked by Facebook.

Given a 32-bit integer, return the number with its bits reversed.

For example, given the binary number 1111 0000 1111 0000 1111 0000 1111 0000, return 0000 1111 0000 1111 0000 1111 0000 1111.
"""

# Clarify whether to return a number in decimal or binary form.

# range of 32-bit integers in 2's complement:
# negative limit = -2^31 = -1 << 31 = 0b100..0 = -0x8000_0000 = −2,147,483,648
# positive limit = 2^31 - 1 = (1 << 31) - 1 = 0b111..1 = 0x7fff_ffff = 2,147,483,647


# Parameter n and return value are in decimal form.
def reverse_bits(n):
    n_str = format(n, '032b')

    r_str = n_str[::-1]
    r = int(r_str, base=2)

    neg_limit = -1 << 31
    pos_limit = (1 << 31) - 1

    if (r >= neg_limit) and (r <= pos_limit):
        return r
    else:
        return 0


n = 1000
r = reverse_bits(n)

print("\nn = {}".format(n))
print("r = {}".format(r))

print("\nn binary = {0:032b}".format(n))
print("r binary = {0:032b}".format(r))

### This also works:
# print("\nn binary = " + format(n, '032b'))
# print("r binary = " + format(r, '032b'))


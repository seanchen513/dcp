"""
dcp161
LC190 easy

This problem was asked by Facebook.

Given a 32-bit integer, return the number with its bits reversed.

For example, given the binary number 1111 0000 1111 0000 1111 0000 1111 0000, return 0000 1111 0000 1111 0000 1111 0000 1111.
"""

# Clarify whether to return a number in decimal or binary form.

"""
Range of 32-bit integers in 2's complement:

negative limit = -2^31 = -1 << 31 = 0b100..0 = -0x8000_0000 = −2,147,483,648

positive limit = 2^31 - 1 = (1 << 31) - 1 = 0b111..1 = 0x7fff_ffff = 2,147,483,647
"""

"""
Solution#1: use string
Parameter n and return value are in decimal form.
"""
def reverse_bits(n):
    #s = format(n, '032b')
    s = "{:032b}".format(n)
    #s = f"{n:032b}"

    return int(s[::-1], base=2)

    # neg_limit = -1 << 31
    # pos_limit = (1 << 31) - 1

    #if (r >= neg_limit) and (r <= pos_limit):
    #    return r
    #else:
    #    return 0

"""
Solution#2: bit manipulation
"""
def reverse_bits2(n):
    r = 0

    for _ in range(32):
        r = (r << 1) + (n & 1)
        n >>= 1

    return r

###############################################################################

if __name__ == "__main__":
    n = 1000 # 398458880
    #n = 43261596 # 964176192
    #n = 4294967293 # 3221225471
    #n = 0 # 0 ???

    r1 = reverse_bits(n)
    r2 = reverse_bits2(n)

    print("\nn = {}".format(n))
    print("r1 (string)    = {}".format(r1))
    print("r2 (bit manip) = {}".format(r2))

    print("\nn binary  = {:032b}".format(n))
    print("r1 binary = {:032b}".format(r1))

    ### This also works:
    # print("\nn binary = " + format(n, '032b'))
    # print("r binary = " + format(r, '032b'))

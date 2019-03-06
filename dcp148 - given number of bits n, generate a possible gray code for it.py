"""
dcp#148

This problem was asked by Apple.

Gray code is a binary code where each successive value differ in only one bit, as well as when wrapping around. Gray code is common in hardware so that we don't see temporary spurious values during transitions.

Given a number of bits n, generate a possible gray code for it.

For example, for n = 2, one gray code would be [00, 01, 11, 10].
"""

# https://en.wikipedia.org/wiki/Gray_code#Constructing_an_n-bit_Gray_code


# helper function for Solution #1
def create_gray_code_from_previous(code):
    new_left_list = []
    new_right_list = []

    for x in code:
        new_left_list.append('0' + x)

    for x in reversed(code):
        new_right_list.append('1' + x)

    return new_left_list + new_right_list


# Solution #1:
# assume integer n >= 1
def create_gray_code(n):
    code = ['0', '1']

    for i in range(1, n):
        code = create_gray_code_from_previous(code)

    return code


# Solution #2:
# https://www.geeksforgeeks.org/generate-n-bit-gray-codes-set-2/
#
# Let bits be ordered (MSB -> LSB) 1, 2, 3, ..., n  
# First bit (MSB) of gray code same as first bit of binary rep.
# For all other bits, kth bit of gray code = XOR of kth and (k-1)th bits of binary rep.
def create_gray_code2(n):
    code = []

    for i in range(0, 2**n):
        b = str(bin(i))[2:]

        g = b[0]

        for k in range(1, len(b)-1):
            g = g + str(int(b[k]) ^ int(b[k+1]))

        code.append(g)


n = 4
code = create_gray_code(n)
#code = create_gray_code2(n)

print(code)


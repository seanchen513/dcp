"""
dcp#109

This problem was asked by Cisco.

Given an unsigned 8-bit integer, swap its even and odd bits. The 1st and 2nd bit should be swapped, the 3rd and 4th bit should be swapped, and so on.

For example, 10101010 should be 01010101. 11100010 should be 11010001.

Bonus: Can you do this in one line?
"""

# Solution #1
#
# 00 - 00
# 11 - 11
# 01 - 10
#
def swap_bits(n):
    k = 0

    for i in range(0, 7, 2):
        n2 = (0b11 << i) & n
        #print("n2 = {:08b}".format(n2))

        if n2 == 0b01 << i:
            n2 = 0b10 << i
        elif n2 == 0b10 << i:
            n2 = 0b01 << i

        #print("n2 after = {:08b}".format(n2))
        k |= n2
        #print("k after k |= n2 = {:08b}".format(k))
        #print("="*80)

    return k

# Solution #2
# Shift event bits right 1; shift odd bits left 1
# Even bits: 0b10101010 == 0xAA
# Odd bits: 0b01010101 == 0x55
def swap_bits2(n):
    #return ((n & 0xAA) >> 1) & ((n & 0x55) << 1)
    return ((n & 0b10101010) >> 1) | ((n & 0b01010101) << 1)



n = 0b11111111 # 11111111
n = 0b00000000 # 00000000

n = 0b10101010 # 01010101
n = 0b11100010 # 11010001

k = swap_bits2(n)
print("n = {:08b}".format(n))
print("k = {:08b}".format(k))


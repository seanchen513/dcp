"""
dcp#176
dip#125 (12/12/19)

This problem was asked by Bloomberg.

Determine whether there exists a one-to-one character mapping from one string s1 to another s2.

For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.

Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.
"""

# O(n) time, O(n) space
def char_map(s1, s2):
    if len(s1) != len(s2):
        return None

    d = {}
    i = 0

    for ch in s1:
        if ch in d:
            if s2[i] != d[ch]:
                return None
        else:
            d[ch] = s2[i]
            i += 1

    return d


s1 = "abc"
s2 = "bcd"
m = char_map(s1, s2)
print("\ns1 = {}".format(s1))
print("s2 = {}".format(s2))
print("char map = {}".format(m))

s1 = "foo"
s2 = "bar"
m = char_map(s1, s2)
print("\ns1 = {}".format(s1))
print("s2 = {}".format(s2))
print("char map = {}".format(m))

s1 = "aac"
s2 = "bcd"
m = char_map(s1, s2)
print("\ns1 = {}".format(s1))
print("s2 = {}".format(s2))
print("char map = {}".format(m))






"""
dcp#108

This problem was asked by Google.

Given two strings A and B, return whether or not A can be shifted some number of times to get B.

For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.
"""

# Idea: s1 and s2 are rotations of each other <=> (s2 is substring of s1 + s1 AND len(s1)==len(s2))
def are_rotations(s1, s2):
    if len(s1) != len(s2):
        return False

    return s2 in s1 + s1


s1 = "abcdef"
s2 = "cdefab"
s3 = "cdefba"

b12 = are_rotations(s1, s2)
b13 = are_rotations(s1, s3)

print("\ns1 = {}".format(s1))
print("s2 = {}".format(s2))

print("are rotations of each other?: {}".format(b12))

print("\ns1 = {}".format(s1))
print("s3 = {}".format(s3))
print("are rotations of each other?: {}".format(b13))

s4 = "fab"
b14 = are_rotations(s1, s4)
print("\ns1 = {}".format(s1))
print("s4 = {}".format(s4))
print("are rotations of each other?: {}".format(b14))

s = "x"
b = are_rotations(s, s)
print("\ns = {}".format(s))
print("is rotation of itself?: {}".format(b))


s = "xyz"
b = are_rotations(s, s)
print("\ns = {}".format(s))
print("is rotation of itself?: {}".format(b))


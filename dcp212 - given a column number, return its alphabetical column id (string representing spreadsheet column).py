"""
dcp#212

This problem was asked by Dropbox.

Spreadsheets often use this alphabetical encoding for its columns: "A", "B", "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....

Given a column number, return its alphabetical column id. For example, given 1, return "A". Given 27, return "AA".
"""

# There is no letter acting like a zero would in, say, a hexadecimal expansion.


# Assume n is positive integer.
# O(log n) time
# O(n) space for list and strings
def column_num_to_id(n):
    code = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base = len(code)
    id = []

    while n > 0:
        letter = code[(n-1) % base]
        id.append(letter)
        n = (n-1) // base # result is different because of (n-1) only for cases of 'Z'

    return ''.join(reversed(id))


#n = 1 # A
#n = 26 # Z
n = 27 # AA
#n = 52 # AZ, 26*1 + 26
#n = 53 # BA, 26*2 + 1
#n = 702 # ZZ, 26*26 + 26
#n = 703 # AAA, 1*26^2 + 1 * 26^1 + 1 = 26^2 + 26 + 1
#n = 18278 # ZZZ
#n = 18279 # AAAA = 26^3 + 26^2 + 26 + 1

# letter_ord * base^(pos from right)

id = column_num_to_id(n)

print("n = {}".format(n))
print("id = {}".format(id))


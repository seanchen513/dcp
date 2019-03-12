"""
dcp#159

This problem was asked by Google.

Given a string, return the first recurring character in it, or null if there is no recurring character.

For example, given the string "acbbac", return "b". Given the string "abcdef", return null.
"""

# Clarify meaning of first recurring character.
# When there is more than one pair of such characters, is "first" based on the
# position of the first char in each pair, or the second char in each pair?
# Most likely, it's based on the second char in each pair.


# O(n^2)
def first_recurring_char(str):
    for i in range(0, len(str)):
        for j in range(0, i):
            if s[i] == s[j]:
                return s[i]

    return None


# O(n) using Python set (based on hash table)
def first_recurring_char2(str):
    char_set = set()

    for x in str:
        if x in char_set:
            return x
        else:
            char_set.add(x)

    return None


def test(str):
    #ch = first_recurring_char2(s)
    ch = first_recurring_char2(s)

    print("\nstring = {}".format(s))
    if ch is None:
        print("No recurring characters.")
    else:
        print("First recurring character = {}".format(ch))


s = "acbbac"
test(s) # should be "b"

s = "abcdef"
test(s) # should be None


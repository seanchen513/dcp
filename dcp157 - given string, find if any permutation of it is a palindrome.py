"""
dcp#157
dip#132

This problem was asked by Amazon.

Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, since it can be rearranged to form racecar, which is a palindrome. daily should return false, since there's no rearrangement that can form a palindrome.
"""

# Naive way is to generate every permutation of the string,
# and check each one to see if it's a palindrome.

"""
Solution:
Since we know every permutation is available, we can just
count characters in the string.

If len(string) is even, every character in it should appear
an even number of times in order for the string to be palindrome.

If len(string) is odd, one character will appear an odd number
of times, and every other character will appear an even number of times.

O(n) time
O(n) space for dict
"""
def some_perm_is_palindrome(str):
    d = {} # dict to count chars in string

    # Count chars in str
    for ch in str:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1

    # Even number of chars in str
    # Check if there are any chars with an odd count
    if len(str) % 2 == 0:
        # for n in d.values():
        #     if n % 2 == 1:
        #         return False
        
        # return True

        return not any((n % 2 == 1) for n in d.values())

    # Odd number of chars in str
    # Check how many chars have an odd count

    num_odd = 0
    for n in d.values():
        if n % 2 == 1:
            num_odd += 1

            if num_odd > 1: # early return
                return False

    # num_odd = sum((n % 2) for n in d.values()) # no early return

    return num_odd == 1


###############################################################################

strings = ["", "a", "ab", "abb", "aabb", "abbc", "abbcc",
    "carrace", "racecar", # palindromes
    "daily", "google",
    ]

for s in strings:
    b = some_perm_is_palindrome(s)
    print("{}\t\t{}".format(s, b))


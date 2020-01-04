"""
dcp#46

This problem was asked by Amazon.

Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".
"""


def longest_palindrome_length(s, max_so_far=0):
    end = len(s) - 1
    if end <= 0:
        return end + 1

    if s[0] == s[end]:
        return max(2 + longest_palindrome_length(s[1:end], max_so_far - 1), max_so_far)

    max_so_far = 0

    return max(longest_palindrome_length(s[1:], max_so_far - 1), \
        longest_palindrome_length(s[:end], max_so_far - 1), \
        max_so_far)


def is_palindrome(s):
    start = 0
    end = len(s) - 1
    
    while (start <= end) and (s[start] == s[end]):
        start += 1
        end -= 1

    if start > end:
        return True
    
    return False

# Solution:
# Find length of longest palindrome first, then check each substring of
# that length within original string.
def longest_palindrome(s):
    n = len(s)
    pal_len = longest_palindrome_length(s)

    #for i in range(n - pal_len + 1):
    for i in range(n):
        substr = s[i : i + pal_len]

        if is_palindrome(substr):
            return substr


###############################################################################


strings = ["", "a", "ab", "abc",
    "elgoog", "google", "apple", "facebook",
    "coffee", "nancy", "pizza", "apple",
    "bosonic", "photon",
    "aabcdcb", "bananas"]

for s in strings:
    #p = longest_palindrome_length(s)
    p = longest_palindrome(s)

    print("{}, {}".format(s, p))



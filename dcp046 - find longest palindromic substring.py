"""
dcp#46

This problem was asked by Amazon.

Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".
"""


def longest_palindrome_length(s):
    start = 0
    end = len(s) - 1

    while (start <= end)  and (s[start] == s[end]):
        start += 1
        end -= 1

    if start > end:
        return len(s)

    return max( 
        longest_palindrome_length(s[1:]), \
        longest_palindrome_length(s[:end]) )


def is_palindrome(s):
    start = 0
    end = len(s) - 1
    
    while (start <= end) and (s[start] == s[end]):
        start += 1
        end -= 1

    if start > end:
        return True
    
    return False

# Solution #1:
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


# Solution #2:
# Essentially the same solution, but combine the methods used
# in the first solution.
def longest_palindrome2(s):
    start = 0
    end = len(s) - 1

    # check if "s" is a palindrome
    while (start <= end)  and (s[start] == s[end]):
        start += 1
        end -= 1

    if start > end:
        return len(s), s

    # "s" is not a palindrome, so...
    l1, s1 = longest_palindrome2(s[1:])
    l2, s2 = longest_palindrome2(s[:end])

    if l1 > l2:
        return l1, s1
    else:
        return l2, s2


# Solution #3:
# Same as #2 but pass start and end indices for substrings to check
# rather than passing substrings themselves.
def longest_palindrome3(s, start, end):
    start2 = start
    end2 = end

    # check if "s" is a palindrome
    while (start2 <= end2)  and (s[start2] == s[end2]):
        start2 += 1
        end2 -= 1

    if start2 > end2: # "s" is a palindrome
        return start, end

    # "s" is not a palindrome, so...
    pal_start1, pal_end1 = longest_palindrome3(s, start + 1, end)
    pal_start2, pal_end2 = longest_palindrome3(s, start, end - 1)

    if pal_end1 - pal_start1 > pal_end2 - pal_start2:
        return pal_start1, pal_end1
    else:
        return pal_start2, pal_end2


###############################################################################


strings = ["", "a", "ab", "abc",
    "abb", "baa",
    "elgoog", "google", "apple", "facebook",
    "coffee", "nancy", "pizza", "apple",
    "bosonic", "photon",
    "aabcdcb", "bananas", 
    "sxgoogys", "sxgoogabcananapq"]

for s in strings:
    #p = longest_palindrome_length(s)
    
    ###
    #p = longest_palindrome(s)
    #print("{}, {}".format(s, p))
    
    ###
    # length, pal = longest_palindrome2(s)
    # print("{}, {}, {}".format(s, length, pal))
    
    ###
    start, end = longest_palindrome3(s, 0, len(s) - 1)
    length = end - start + 1
    print("{}, {}, {}, {}".format(s, length, s[start:end+1], start))


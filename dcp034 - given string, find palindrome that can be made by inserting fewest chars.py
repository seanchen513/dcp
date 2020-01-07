"""
dcp#34

This problem was asked by Quora.

Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".
"""

"""
google
    e-googl-e
        eg-oogl-ge
            egl-oog-lge
                eglg-oo-glge [NOT solution, but output from palindrome_add()]

race
    e-rac-e
        ec-ra-ce
            eca-r-ace

abc
    a-bc-a
        ab-c-ba

abcd
    a-bcd-a
        ab-cd-ba
            abc-d-cba

"""

# NOT a solution.
# Creates palindrome, but not necessarily of shortest length.
# Namely, when string begins or ends with a palindromic substring of length >= 2.
# Eg, "google" returns "eglgooglge".
# However, the solution palindrome_fewest_chars() below builds on this case.
def palindrome_add(s):
    end = len(s) - 1
    if end <= 0:
        return s

    if s[0] < s[end]:
        return palindrome_add(s + s[0])

    if s[0] > s[end]:
        return palindrome_add(s[end] + s)

    return s[0] + palindrome_add(s[1:end]) + s[end]


###############################################################################

# from dcp46 - returns start and end indices of longest palindromic susbtring
def longest_palindrome(s, start, end):
    start2 = start
    end2 = end

    # check if "s" is a palindrome
    while (start2 <= end2)  and (s[start2] == s[end2]):
        start2 += 1
        end2 -= 1

    if start2 > end2: # "s" is a palindrome
        return start, end

    # "s" is not a palindrome, so...
    pal_start1, pal_end1 = longest_palindrome(s, start + 1, end)
    pal_start2, pal_end2 = longest_palindrome(s, start, end - 1)

    # if use >, then "abc" returns "a"
    # if use >=, then "abc" returns "c"
    if pal_end1 - pal_start1 > pal_end2 - pal_start2:
        return pal_start1, pal_end1
    else:
        return pal_start2, pal_end2


# Idea: check for longest palindromic substring...
def palindrome_fewest_chars(s):
    start, end = longest_palindrome(s, 0, len(s) - 1)
    length = end - start + 1

    ### next two "if" statements restrict by length > 1
    ### so that when length is 1, we default to using
    ### palindrome_add(), which will return
    ### ***lexico- earliest*** result.

    # eg, "google" -> "el" + "google"
    # palindromic substring: start = 0, end = 3
    if (start == 0) and (length > 1):
        return s[-1:end:-1] + s

    # eg, "fuzz" -> "fuzz" + "uf"
    # palindromic substring: start = 2, end = 3
    if (end == len(s) - 1) and (length > 1):
        return s + s[start-1::-1] 

    # string doesn't start or end with a palindrome
    return palindrome_add(s)


###############################################################################


strings = ["", # ""
    "a", # "a"
    "ab", # "aba"
    "abc", # "abcba"
    "cba", # "abcba"

    "abb", # "abba"
    "aab", # "baab", NOT "aabaa"
    "baa", # "baab", NOT "aabaa"
    "bba", # "abba"
    
    "abcda", # "abcdadcba", NOT "adcbabcda"
    "abcde", # "abcdedcba", NOT "edcbabcde"

    "fuzz", # "fuzzuf"
    "racecar", # "racecar" -- already a palindrome
    "race", # "ecarace", NOT "racecar"
    "google", # "elgoogle" -- note inner palindrome "goog"
    "tagoogle" # "elgoogatagoogle"
    ]


for s in strings:
    #p_add = palindrome_add(s)
    start, end = longest_palindrome(s, 0, len(s) - 1)
    p = palindrome_fewest_chars(s)

    #print("{}\t\t{}".format(s, p_add))
    print("{}\t\t{}\t\t{}".format(s, p, s[start:end+1]))
    


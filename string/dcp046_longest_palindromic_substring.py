"""
dcp46
LC5 medium

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
        longest_palindrome_length(s[:-1]) ) # 1/14/20 fix: was "s[:end]"


def is_palindrome(s):
    start = 0
    end = len(s) - 1
    
    while (start <= end) and (s[start] == s[end]):
        start += 1
        end -= 1

    if start > end:
        return True
    
    return False

"""
Solution #1:
Find length of longest palindrome first, then check each substring of
that length within original string.

Takes too long on:
"babaddtattarrattatddetartrateedredividerb" # LC: "ddtattarrattatdd"
"""
def longest_palindrome(s):
    n = len(s)
    pal_len = longest_palindrome_length(s)

    #for i in range(n - pal_len + 1):
    for i in range(n):
        substr = s[i : i + pal_len]

        if is_palindrome(substr):
            return substr

"""
Solution #2:
Essentially the same solution, but combine the methods used
in the first solution.

Takes too long on:
"babaddtattarrattatddetartrateedredividerb" # LC: "ddtattarrattatdd"
"""
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
    l2, s2 = longest_palindrome2(s[:-1]) # 1/14/20 fix: was "s[:end]"

    if l1 > l2:
        return l1, s1
    else:
        return l2, s2

"""
Solution #3:
Same as #2 but pass start and end indices for substrings to check
rather than passing substrings themselves.
"""
def longest_palindrome3(s, start=0, end=None):
    if end is None:
        start = 0
        end = len(s) - 1

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

"""
Solution: Check larger substrings first, and only check if substring
length is larger than max length of any palindrome found so far.
"""
def longest_palindrome4(s):
    n = len(s)
    max_start = 0
    max_end = 0

    for i in range(n):
        for j in range(n-1, i, -1):
            if j - i <= max_end - max_start:
                break

            if is_palindrome(s[i:j+1]):
                max_start = i
                max_end = j

    return s[max_start : max_end + 1]

"""
Solution: ...
LC: time exceeded
"""
def longest_palindrome5(s):
    n = len(s)
    if n <= 1:
        return s

    for length in range(n, 0, -1):
        for start in range(n - length + 1):
            if is_palindrome(s[start:start+length]):
                return s[start : start+length]


"""
Solution:
Uses dict and only checks substrings that start and end with
the same letter.

Not much faster...
"""
def longest_palindrome6(s):
    n = len(s)
    d = {}

    for i in range(n):
        if s[i] in d:
            d[s[i]].append(i)
        else:
            d[s[i]] = [i]

    ###
    max_start = 0
    max_end = 0

    for v in d.values():
        if len(v) < 2:
            continue

        n = len(v)

        for i in range(n):
            for j in range(n-1, i, -1):
                if v[j] - v[i] <= max_end - max_start:
                    break

                if is_palindrome(s[v[i]:v[j]+1]):
                    max_start = v[i]
                    max_end = v[j]

    return s[max_start : max_end + 1]

###############################################################################
"""
Solution: Dynamic Programming (LC)

P(i, j) = True if s[i:j+1] is palindrome, else False

P(i, j) = ( P(i+1, j-1) and s[i] == s[j] )

Base cases:
P(i, i) = True
P(i, i+1) = ( s[i] == s[i+1] )

O(n^2) time
O(n^2) space
"""
def longest_palindrome7(s):
    n = len(s)
    p = [[False]*n for _ in range(n)]

    for i in range(n):
        p[i][i] = True

    max_start = 0
    max_end = 0

    for i in range(n-1):
        p[i][i+1] = (s[i] == s[i+1])
        if p[i][i+1]:
            max_start = i
            max_end = i + 1

    ###

    for d in range(2, n):
        for i in range(n - d):
            p[i][i+d] = p[i+1][i+d-1] and (s[i] == s[i + d])

            if p[i][i+d]:
                if d > max_end - max_start:
                    max_start = i
                    max_end = i + d

    return s[max_start : max_end + 1]

###############################################################################
"""
Solution: expand around center

2n - 1 centers: 
n letters for odd-length palindromes
n - 1 spaces between letters for even-length palindromes

Each expansion takes O(n) time.

O(n^2) time
O(1) space
"""

def expand_around_center(s, left, right):
    n = len(s)
    l = left
    r = right
    
    while (l >= 0) and (r < n) and (s[l] == s[r]):
        l -= 1
        r += 1

    #return r - l - 1
    return l+1, r-1

def longest_palindrome8(s):
    n = len(s)
    max_start = 0
    max_end = 0

    for i in range(n):
        l, r = expand_around_center(s, i, i) # odd-length palindromes

        if r - l > max_end - max_start:
            max_start = l
            max_end = r

        l, r = expand_around_center(s, i, i+1) # even-length palindromes

        if r - l > max_end - max_start:
            max_start = l
            max_end = r

    return s[max_start : max_end + 1]

###############################################################################

strings = [
    "", # ""
    "a", # "a"
    "ab", "abc",
    "abb", "baa",
    "elgoog", "google", "apple", "facebook",
    "coffee", "nancy", "pizza", "apple",
    "bosonic", 
    "photon",
    "aabcdcb", 
    "bananas", 
    "sxgoogys", 
    "sxgoogabcananapq", 
    "aaabaaaa", # LC

    "babaddtattarrattatddetartrateedredividerb", # LC: "ddtattarrattatdd"
    
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", # LC

    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", # LC
    ]

for s in strings:
    p = longest_palindrome8(s)
    print("{}, {}".format(s, p))
    
    ###
    # length, pal = longest_palindrome2(s)
    # print("{}, {}, {}".format(s, length, pal))
    
    ###

    # start, end = longest_palindrome3(s)
    # length = end - start + 1
    # print("{}, {}, {}, {}".format(s, length, s[start:end+1], start))

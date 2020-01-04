"""
dcp#121, 411

This problem was asked by Google.

Given a string which we can delete at most k, return whether you can make a palindrome.

For example, given 'waterrfetawx' and a k of 2, you could delete f and x to get 'waterretaw'.

"""

"""
Notes: just some thoughts here; not implemented.

Initial check... how many chars? how many of each char?

len = 12, so chars 0..11, midpt = 5, 6, avg = 5.5
w 0, 10     avg = 5
a 1, 9      5
t 2, 8      5
e 3, 7      5
r 4, 5      4.5

f 6 - must delete since unpaired and len even
x 11 - must delete since unpaired and len even

After 2 deletions, chars are 0..9, avg = 4.5
In general, if len odd, min deletions = num chars w/ odd count.

If len odd, must have exactly one char with odd # count.
Min deletions = (num chars w/ odd count) - 1. (???)

Drawback: this relies on examining every char in string, which 
can be bad if string is very long, eg, 100k chars.
"""

# Assume empty string is a palindrome.
# Argument "depth" is for learning purposes.
def del_palindrome(s, k, depth=0):
    end = len(s) - 1
    
    # If s is empty string, then end is -1.
    # If end is 0, then s is 1-char string.
    if end <= 0: 
        return True
    
    print("    "*depth + "{}, k = {}, depth = {}".format(s, k, depth))

    if s[0] == s[end]:
        return del_palindrome(s[1:end], k, depth+1)

    else: 
        if k == 0: # ends of string don't match, and no more deletions allowed
            #print("    "*depth + "### Ran out of allowed deletions")
            return False
        else: # try deleting 1st char or last char
            return del_palindrome(s[1:], k-1, depth+1) or del_palindrome(s[:end], k-1, depth+1)


# Optimized so recursion isn't used until a deletion is needed.
def del_palindrome2(s, k, depth=0):
    end = len(s) - 1
    if end <= 0:
        return True

    print("    "*depth + "{}, k = {}, depth = {}".format(s, k, depth))

    start = 0
    while s[start] == s[end]:
        start += 1
        end -= 1

        if start >= end:
            return True

    if k <= 0:
        #print("    "*depth + "### Ran out of allowed deletions")
        return False
    
    # try deleting 1st char or last char
    return del_palindrome2(s[start+1:end+1], k-1, depth+1) \
        or del_palindrome2(s[start:end], k-1, depth+1)


"""
Try using start and end arguments instead of passing sliced strings.
Seems to be faster, but not by orders of magnitude (tested without print).
Tested with input like:
s = "abc"*100
k = 20
"""
def del_palindrome3(s, start, end, k, depth=0):
    if end <= 0:
        return True

    print("    "*depth + "{}, k = {}, depth = {}".format(s[start:end+1], k, depth))

    while s[start] == s[end]:
        start += 1
        end -= 1

        if start >= end:
            return True

    if k <= 0:
        #print("    "*depth + "### Ran out of allowed deletions")
        return False
    
    # try deleting 1st char or last char
    return del_palindrome3(s, start+1, end, k-1, depth+1) \
        or del_palindrome3(s, start, end-1, k-1, depth+1)


###############################################################################

from timeit import default_timer as timer

s = ""
s = "x"
s = "xx"
s = "xy"
s = "xzzy"
s = "waterrfetawx"
k = 2

#s = "abc"*100
#k = 20

print("\nstring = {}".format(s))
print("k = {}".format(k))

import sys
recursion_limit = sys.getrecursionlimit() # I get 1000
print("\nDefault recursion limit = {}".format(recursion_limit))

recursion_limit = 30
sys.setrecursionlimit(recursion_limit)
print("Setting recursion limit to {}\n".format(recursion_limit))

### take out print's from function if timing
#start = timer()

#p = del_palindrome(s, k)
p = del_palindrome2(s, k)
#p = del_palindrome3(s, 0, len(s)-1, k)

#end = timer()
#print("\nTime: {}".format(end - start))

print("\n{}".format(p))


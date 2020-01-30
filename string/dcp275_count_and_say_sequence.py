"""
dcp275 (medium)

This problem was asked by Epic.

The "look and say" sequence is defined as follows: beginning with the term 1, each subsequent term visually describes the digits appearing in the previous term. The first few terms are as follows:

1
11
21
1211
111221
As an example, the fourth term is 1211, since the third term consists of one 2 and one 1.

Given an integer N, print the Nth term of this sequence.
"""

"""
38. Count and Say
Easy

The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. You can do so recursively, in other words from the previous member read off the digits, counting the number of digits in groups of the same digit.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Explanation: This is the base case.

Example 2:

Input: 4
Output: "1211"
Explanation: For n = 3 the term was "21" in which we have two groups "2" and "1", "2" can be read as "12" which means frequency = 1 and value = 2, the same way "1" is read as "11", so the answer is the concatenation of "12" and "11" which is "1211".
"""

###############################################################################
"""
Solution #1: recursion
"""
def count_say(n):
    if n == 1:
        return "1"

    s = count_say(n-1)
    t = ""
    
    prev = s[0]
    count = 1

    for i in range(1, len(s)):
        if  s[i] == prev:
            count += 1
        else:
            t += str(count) + prev
            count = 1
            prev = s[i]

    # For last iteration: 
    # If s[n-1] == prev (ie, s[n-2]), then count increased, but string t
    # still needs to be updated for the char "prev".
    # If s[n-1] != prev (ie, new char), then string t was updated up to
    # "prev", but still needs to be updated for the new char s[n-1].

    t += str(count) + prev

    return t

###############################################################################
"""
Solution #1b: iterative version of sol #1.
"""
def count_say1b(n):
    s = "1" # base case for n = 1

    for _ in range(n-1):
        t = ""        
        prev = s[0]
        count = 1

        for i in range(1, len(s)):
            if  s[i] == prev:
                count += 1
            else:
                t += str(count) + prev
                count = 1
                prev = s[i]

        s = t + str(count) + prev

    return s

###############################################################################
"""
Solution #2: same as sol #1, but use "t" as a list of strings first,
and then concatenate at the end.
"""
def count_say2(n):
    if n == 1:
        return "1"

    s = count_say(n-1)
    t = []
    
    prev = s[0]
    count = 1

    for i in range(1, len(s)):
        if  s[i] == prev:
            count += 1
        else:
            t.extend([str(count), prev])
            count = 1
            prev = s[i]

    t.extend([str(count), prev])
    
    return ''.join(map(str, t))

###############################################################################
"""
Solution #3: same as sol #1, but get rid of the var "prev".

This seems to be SLOWER.
"""
def count_say3(n):
    if n == 1:
        return "1"

    s = count_say(n-1)
    t = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            t += str(count) + s[i-1]
            count = 1

    t += str(count) + s[-1]

    return t
    
###############################################################################
"""
Solution #4: use itertools.groupby(); iterative.
"""
import itertools

def count_say4(n):
    s = "1" # base case for n = 1

    for _ in range(n-1):
        g = itertools.groupby(s)
        s = ""

        for digit, group in g:
            s += str(len(list(group))) + digit

    return s

###############################################################################
"""
Other solutions using regular expressions...

https://leetcode.com/problems/count-and-say/discuss/15999/4-5-lines-Python-solutions
"""

###############################################################################

if __name__ == "__main__":
    #for k in range(1, 31):
    for k in range(1, 11):
        #s = count_say(k)
        s = count_say1b(k)
        #s = count_say2(k)
        #s = count_say3(k)
        #s = count_say4(k)
        
        print(f"{k:4}: {s}")

"""
dcp123

This problem was asked by LinkedIn.

Given a string, return whether it represents a number. Here are the different kinds of numbers:

"10", a positive integer
"-10", a negative integer
"10.1", a positive real number
"-10.1", a negative real number
"1e5", a number in scientific notation
And here are examples of non-numbers:

"a"
"x 1"
"a -2"
"-"
"""

"""
LC65. Valid Number
Hard

Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
Of course, the context of these characters also matters in the input.
"""

"""
My notes:
- empty string "" is not a valid number
- ignore spaces (always?)
- at most one from {+, -} allowed before "e" and after "e".  It must be the first
symbol in each subexpression.
- at most one "." allowed before "e" (not allowed after "e")
- "." can have digits on just one side or both sides; eg, ".1", "1.", "1.2"
- "e" is only letter allowed; it can appear at most once;
it must be preceded by a valid number and followed by an integer
(pos, neg, or 0).

Idea:
1. Get rid of spaces (and other whitespace).
2. Check for any invalid characters.
3. Check for letters.  There should be at most one "e".
4. If there is an "e", check left and right sides separately.  
Number expression before "e" checked in below steps (same as if there were no "e" at all).
Number after "e" must be integer (pos, neg, or 0), but no decimals (even "2.0")

5. Check for at least one digit (if "e" expression, check for each subexpression)
6. Scan for first symbol.  If "+" or "-", scan if there is another one of either.
If first symbol is neither, scan if "+" or "-" appears after.
7. Check if there is at most one ".".

Other:
According to Python 3.7.1 interpreter:
Valid: "000", "+001e-001"
Invalid: "001"
"""

"""
Solution#1: 
*** Treats "001" as valid, as does LeetCode.  Python 3.7.1 interpreter does not.

LeetCode, Jan 16, 2020:
Runtime: 28 ms, faster than 85.28% of Python3 online submissions for Valid Number.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Valid Number.
"""
def valid_number_string(s : str) -> bool:
    s = s.strip() # remove all whitespace

    n = len(s)

    # num_digits_base = 0
    # num_digits_exp = 0
    digit_count = 0

    e_count = 0 # "e"
    sign_count = 0 # "+" or "-"
    dot_count = 0 # "."

    for i in range(n):
        ch = s[i]

        if (ch >= '0') and (ch <= '9'):
            digit_count += 1
            continue

        if ch == 'e':
            e_count += 1
            if e_count >= 2:
                return False

            #e_pos = i # store position of 'e' so we can split string later

            if digit_count == 0: # this is for base number (before "e")
                return False

            # reset counters, so we can have them count for exponent expression
            digit_count = 0
            sign_count = 0
            dot_count = 0
            continue

        if (ch == '+') or (ch == '-'):
            if (digit_count > 0) or (dot_count > 0):
                return False

            sign_count += 1
            if sign_count >= 2:
                return False

            continue

        if ch == '.':
            if e_count == 1:
                return False # "." not allowed after "e"

            dot_count += 1
            if dot_count >= 2:
                return False

            continue

        return False

    # Case with "e" with base number before "e" already checked inside loop.
    # So this is now for cases (1) no "e", and (2) 2nd "e" subexpression
    if digit_count == 0:
        return False
        
    return True


###############################################################################
"""
Solution #2: use DFA (deterministic finite automaton)

https://leetcode.com/problems/valid-number/discuss/23728/A-simple-solution-in-Python-based-on-DFA
"""
### DO LATER


###############################################################################

if __name__ == "__main__":
    strings = [
        ### LC examples
        ("0", True),
        (" 0.1 ", True),
        ("abc", False),
        ("1 a", False),
        ("2e10", True),
        (" -90e3   ", True),
        (" 1e", False),
        ("e3", False),
        (" 6e-1", True),
        (" 99e2.5 ", False), # exponent must be integer (pos or neg)
        ("53.5e93", True),
        (" --6 ", False), # cannot have more than one sign in non-"e" expression
        ("-+3", False),
        ("95a54e53", False),

        ### more examples; assume no whitespace; following Python interpreter 3.7.1
        ("", False),
        ("e", False),

        ("00", True), # evaluates to 0
        #("001", False), # "SyntaxError: invalid token"
        ("001.", True),
        (".000", True),
        ("000.", True),
        ("+001e-001", True),

        ("+", False), # must have a digit
        
        ("-0", True),
        ("-0e-0", True),
        ("0e0", True),
        ("+0.e+0", True),

        (".1", True),
        ("1.", True),
        ("+3", True),
        ("1+2", False), # sign must be at start of non-"e" expression
        ("12-", False), # sign must be at start of non-"e" expression

        ("1e1", True),
        ("+1.", True),
        ("-.1", True),
        (".1e1", True), 
        ("1e.1", False), # dot not allowed after "e"
        ("1e1.", False), # dot not allowed after "e"
        ("1e1.2", False), # dot not allowed after "e"

        ("1e-2", True), # negative integer exponents ok
        ("1e0", True), # zero exponents ok
        (".1e1", True),
        ("1.e1", True),

        ("1.2.3", False),
        ("1..3", False),
        (".-3", False), # sign must be first symbol; in particular
        ("0.+3", False), # sign must be first symbol; in particular
    ]

    for s in strings:
        valid = valid_number_string(s[0])
        
        print(f"\"{s[0]}\"", valid)
        
        assert(valid == s[1])

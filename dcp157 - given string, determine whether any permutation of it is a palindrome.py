"""
This problem was asked by Amazon.

Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, since it can be rearranged to form racecar, which is a palindrome. daily should return false, since there's no rearrangement that can form a palindrome.
"""

# Naive way is to generate every permutation of the string,
# and check each one to see if it's a palindrome.

# Since we know every permutation is available, we can just
# count characters in the string.
# If len(string) is even, every character in it should appear
# an even number of times in order for the string to be palindrome.
# If len(string) is odd, one character will appear an odd number
# of times, and every other character will appear an even number of times.


def some_perm_is_palindrome(str):
    d = {}

    for x in str:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1

    if len(str) % 2 == 0:
        for x, n in d.items():
            if n % 2 == 1:
                return False
        
        return True

    else: # len(str) is odd
        num_odd = 0
        for x, n in d.items():
            if n % 2 == 1:
                num_odd += 1

        if num_odd == 1:
            return True
        else:
            return False


def test(str):
    b = some_perm_is_palindrome(str)
    print("\nstring = {}".format(str))
    print("is some permutation of it a palindrome?: {}".format(b))


s = "carrace"
test(s)

s = "daily"
test(s)


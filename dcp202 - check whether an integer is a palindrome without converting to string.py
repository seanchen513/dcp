"""
dcp#202

This problem was asked by Palantir.

Write a program that checks whether an integer is a palindrome. For example, 121 is a palindrome, as well as 888. 678 is not a palindrome. Do not convert the integer into a string.
"""

# Assume that we cannot convert to anything else like a list, as well.
# Assume given integer is non-negative, althugh can easily modify code to work for negative ints.


# Assume n is non-negative integer.
# Note -1 // 10 is -1.  But can easily modify code to work for negative ints.
def num_digits(n):
    if n == 0:
        return 1

    k = 0
    while n != 0:
        n //= 10
        k += 1
        #print("n = {}, k = {}".format(n, k))
        
    return k 


def is_palindrome(n):
    num_d = num_digits(n)
    p_ten = 10 ** (num_d - 1) # largest power of 10 that is smaller than n

    while num_d > 1:
        low = n % 10
        high = n // p_ten

        print("\nn = {}".format(n))
        print("high = {}, low = {}".format(high, low))

        if low != high:
            return False
        
        n %= p_ten
        n //= 10
        
        num_d -= 2
        p_ten //= 100

    return True


################################################################################

# not palindromes
n = 10
n = 12341
n = 12345321

# palindromes
n = 0
n = 5
n = 121
n = 1234321
n = 12344321

b = is_palindrome(n)

print("n = {}".format(n))

#num_d = num_digits(n)
#print("num digits = {}".format(num_d))

print("is palindrome? {}".format(b))


"""
dcp#252

This problem was asked by Palantir.

The ancient Egyptians used to express fractions as a sum of several terms where each numerator is one. For example, 4 / 13 can be represented as 1 / 4 + 1 / 18 + 1 / 468.

Create an algorithm to turn an ordinary fraction a / b, where a < b, into an Egyptian fraction.
"""

# Inputs a, b are positive integer numerator and denominator of proper fraction.  (a < b)
# Output is list of denominators in Egyption fraction that is equal to a/b.
def egyption_fraction(a, b):
    denoms = []

    while a != 0:
        if b % a == 0:
            n = int(b/a)
        else:
            n = int(b/a) + 1
        
        denoms.append(n)

        # a/b - 1/n = (a*n - b) / (b*n)
        a = a * n - b
        b = b * n
        #print("n = {}, a = {}, b = {}".format(n, a, b))

    return denoms


# This function has rounding errors that need to be dealt with.
def egyption_fraction2(a, b):
    denoms = []

    x = a/b

    while x != 0:
        n = int(1.0/x) + 1

        denoms.append(n)
        x -= 1.0/n
        print("n = {}, x = {}".format(n, x))

    return denoms



a = 4
b = 13

f = egyption_fraction(a, b)
print(f)


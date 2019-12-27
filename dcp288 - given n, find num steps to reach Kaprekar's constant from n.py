"""
dcp#288

This problem was asked by Salesforce.

The number 6174 is known as Kaprekar's contant, after the mathematician who discovered an associated property: for all four-digit numbers with at least two distinct digits, repeatedly applying a simple procedure eventually results in this value. The procedure is as follows:

For a given input x, create two new numbers that consist of the digits in x in ascending and descending order.
Subtract the smaller number from the larger number.
For example, this algorithm terminates in three steps when starting from 1234:

4321 - 1234 = 3087
8730 - 0378 = 8352
8532 - 2358 = 6174

Write a function that returns how many steps this will take for a given input N.
"""

# Assume n is 4-digit positive integer with at least 2 distinct digits
def kaprekar(n):
    if (n < 1000) or (n > 9999):
        print("Given integer be with [1000, 9998], not all the same.")
        return None

    steps = 0

    while n != 6174:
        inc = ''.join(sorted( d for d in str(n) ))
        dec = inc[::-1]
        
        n = int(dec) - int(inc)
        steps += 1

        if n == 0: # this happens if all the digits of n are the same
            print("Given integer must have at least 2 distinct digits.")
            return None

        print('{} - {} = {}'.format(dec, inc, n))

        if n < 1000: # pad with 0's
            n *= 10
            print("*** pad with 0's")


    return steps


# Recursive
def kaprekar_recurse(n, steps=0):
    if n == 0: # this happens if all the digits of n are the same
        print("Given integer must have at least 2 distinct digits.")
        return None

    if n == 6174:
        return steps
    
    inc = ''.join(sorted( d for d in str(n) ))
    dec = inc[::-1]
    
    n = int(dec) - int(inc)

    print('{} - {} = {}'.format(dec, inc, n))

    if n < 1000: # pad with 0's
        n *= 10
        print("*** pad with 0's")

    return kaprekar_recurse(n, steps + 1)


###############################################################################

"""
Check which numbers need to be padded with 0 and by how many 0's
All the modified numbers that need to be padded are 999 and only need one 0 appended.

There are 68 such numbers, including: 1000, 1011, 1101, ..., 9989, 9998.
They each involve only 2 distinct, consecutive digits.
They each require 5 steps to reach Kaprekar's constant.
They all involve the same numbers after the padding is done.

Example:
9888 - 8889 = 999
pad with 0
9990 - 0999 = 8991
9981 - 1899 = 8082
8820 - 0288 = 8532
8532 - 2358 = 6174

digits - how many?
0, 1: 4, namely 1000, 1011, 1101, 1110
1, 2: 8
2, 3: 8
3, 4: 8
4, 5: 8
5, 6: 8
6, 7: 8
7, 8: 8
8, 9: 8, namely 8889, 8898, 8988, 8999, 9888, 9899, 9989, 9998
"""
def check_kaprekar_pad(n):
    nums = []

    def kaprekar(n):
        orig = n

        while n != 6174:
            inc = ''.join(sorted( d for d in str(n) ))
            dec = inc[::-1]
            
            n = int(dec) - int(inc)

            if n == 0: # this happens if all the digits of n are the same
                return None

            pad = 0
            if n < 1000: # pad with 0's
                n *= 10
                pad += 1
                nums.append(orig)
                print("n = {}, pad = {}, n* = {}".format(orig, pad, n))

        #return steps

    for n in range(1000, 9999):
        kaprekar(n)

    print()
    print(nums)
    print("\nhow many? {}".format(len(nums)))


"""
At most 7 steps are required to reach Kaprekar's constant.

Calculate how many numbers in [1000, 9999] require
a certain number of steps to get to Kaprekar's constant.
Required number of steps are in the range [1, 7].

Numbers that lead to 0 are assigned -1 as the number of steps.
There are 9 of these: 1111, 2222, ..., 9999.

Kaprekar's constant itself requires 0 steps trivially.

Distribution:
-1: 9
0: 10
1: 356
2: 519
3: 2124
4: 1124
5: 1379
6: 1508
7: 1980
"""
def kaprekar_steps_distrib():
    def kaprekar(n):
        steps = 0
        
        while n != 6174:
            inc = ''.join(sorted( d for d in str(n) ))
            dec = inc[::-1]
            
            n = int(dec) - int(inc)
            steps += 1

            if n == 0: # this happens if all the digits of n are the same
                return -1

            if n < 1000: # pad with 0's
                n *= 10

        return steps

    max_steps = 0
    steps = {-1: 0, 0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}

    for n in range(1000, 10000):
        num_steps = kaprekar(n)
        steps[num_steps] += 1

        if steps is not None:
            max_steps = max(num_steps, max_steps)

    print("\nmax steps = {}".format(max_steps))
    print("\nsteps:")
    print(steps)

    return max_steps

###############################################################################

#n = 1111
#n = 1110
#n = 1000
#n = 9888
n = 1234

print("\nn = {}\n".format(n))

num_steps = kaprekar(n)
#num_steps = kaprekar_recurse(n)

print("\nnumber of steps to reach Kaprekar's constant 6174: {}".format(num_steps))

#check_kaprekar_pad(n)
#kaprekar_steps_distrib()


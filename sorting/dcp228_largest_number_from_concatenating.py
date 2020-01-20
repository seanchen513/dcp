"""
dcp228

This problem was asked by Twitter.

Given a list of numbers, create an algorithm that arranges them in order to form the largest possible integer. For example, given [10, 7, 76, 415], you should return 77641510.
"""

"""
LC179. Largest Number
Medium

Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"

Example 2:

Input: [3,30,34,5,9]
Output: "9534330"

Note: The result may be very large, so you need to return a string instead of an integer.
"""

import typing

"""
Solution #1: brute force.  Look at all permutations.
Uses recursion and backtracking.

"a" = array of integers
"left" = left index of array

O(n!) time
"""
def largest_int(a, left=0, max_int=0):
    n = len(a)

    if left == n - 1:
        k = int(''.join(map(str, a)))
        max_int = max(k, max_int)
    
    else:
        for i in range(left, n):
            a[left], a[i] = a[i], a[left]
            
            max_int = largest_int(arr, left + 1, max_int)
            
            a[left], a[i] = a[i], a[left] # backtrack

    return max_int

################################################################################
"""
Solution #1b: same idea as sol #1, but use itertools.permutations() and iteration.

Faster than sol #1.
"""

import itertools

def largest_int1b(a):
    if not a:
        return 0

    max_int = 0

    for perm in itertools.permutations(a):
        k = int(''.join(map(str, perm)))
        max_int = max(max_int, k)

    return max_int

################################################################################
"""
Solution #2: Sort using custom comparison function.  Since the comparison
works by comparing strings, we convert all the integers in the 
input array to strings first.

Notes
- If arr is [], then empty string is returned.
- If arr is [0, 0], then "0" should be returned, not "00".

O(n log n) time due to sorted()
O(n) extra space for storing sorted entries.

Much faster than sol #1b.
"""
import functools

def largest_int2(arr):
    arr = map(str, arr)

    ### Use custom comparator (2 args), but convert to key for sorted() using 
    ### functools.cmp_to_key().
    ### This seems to be faster than using a custom key class directly.
    s = sorted(arr, key=functools.cmp_to_key(comparator2))

    ### Use custom key class directly.  The key class defines __lt__().
    ### This seems to be slower than using a custom comparison function.
    #s = sorted(arr, key=test_key)

    if s[0] == 0: # happens if input array contained only 0's
        return "0"

    return ''.join(s)

def comparator(x, y):
    xy = str(x) + str(y)
    yx = str(y) + str(x)
    
    return int(yx) - int(xy)

# Same as comparator(), but work with string versions of integers.
def comparator2(x: str, y: str) -> int:   
    return int(y + x) - int(x + y)

"""
https://docs.python.org/3/howto/sorting.html
"In Python 3.2, the functools.cmp_to_key() function was added to the
functools module in the standard library."

def cmp_to_key(mycmp):
    # Convert a cmp= function into a key= function
    class K:
        #def __init__(self, obj, *args):
        def __init__(self, obj):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        # def __gt__(self, other):
        #     return mycmp(self.obj, other.obj) > 0
        # def __eq__(self, other):
        #     return mycmp(self.obj, other.obj) == 0
        # def __le__(self, other):
        #     return mycmp(self.obj, other.obj) <= 0
        # def __ge__(self, other):
        #     return mycmp(self.obj, other.obj) >= 0
        # def __ne__(self, other):
        #     return mycmp(self.obj, other.obj) != 0
    return K
"""

# Code key class directly for use with key parameter in sorted()
class test_key():
    def __init__(self, obj):
        self.obj = obj

    def __lt__(self, other):
        xy = str(self.obj) + str(other.obj)
        yx = str(other.obj) + str(self.obj)
        
        return int(yx) < int(xy)

################################################################################
"""
Same as solution #2, but deal with ints.
"""

def largest_int2b(arr):
    #arr = map(str, arr)

    ### Use custom comparator (2 args), but convert to key for sorted() using 
    ### functools.cmp_to_key().
    ### This seems to be faster than using a custom key class directly.
    s = sorted(arr, key=functools.cmp_to_key(comparator))

    ### Use custom key class directly.  The key class defines __lt__().
    ### This seems to be slower than using a custom comparison function.
    #s = sorted(arr, key=test_key)

    #return int( ''.join([str(x) for x in s]) )
    return int( ''.join(map(str, s)) )
    

################################################################################

if __name__ == "__main__":
    #arr = []
    #arr = [1]
    #arr = [10, 2] # LC ex1, answer "210"
    #arr = [1, 2, 3]
    #arr = [10, 7, 76, 415]
    #arr = [3, 30, 34, 5, 9] # LC ex2, answer "9534330"

    import random
    arr = [random.randint(0,19) for _ in range(5)]    

    print("\nlist of numbers = {}".format(arr))

    n = largest_int(arr)
    print("\nlargest int (sol #1) = {}".format(n))

    n1b = largest_int1b(arr)
    print("\nlargest int (sol #1b) = {}".format(n1b))

    n2 = largest_int2(arr)
    print("\nlargest int (sol #2) = {}".format(n2))
    
    n2b = largest_int2(arr)
    print("\nlargest int (sol #2b) = {}".format(n2b))

    ###

    import timeit

    t1 = timeit.timeit("n = largest_int(arr)", "from __main__ import largest_int, arr", number=1000)
    t1b = timeit.timeit("n = largest_int1b(arr)", "from __main__ import largest_int1b, arr", number=1000)
    t2 = timeit.timeit("n = largest_int2(arr)", "from __main__ import largest_int2, arr", number=1000)
    t2b = timeit.timeit("n = largest_int2b(arr)", "from __main__ import largest_int2b, arr", number=1000)

    print(f"\nt1   = {t1}")
    print(f"\nt1b  = {t1b}")
    print(f"\nt2   = {t2}")
    print(f"\nt2b  = {t2b}")

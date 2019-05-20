"""
dcp#228

This problem was asked by Twitter.

Given a list of numbers, create an algorithm that arranges them in order to form the largest possible integer. For example, given [10, 7, 76, 415], you should return 77641510.
"""

# Naive solution: look at all permutations.
# Uses backtracking.
# "a" = array of integers
# "l" = left index of array
# O(n!)
def largest_int(a, l=0, max_int=0):
    n = len(a)

    if l == n - 1:
        k = int(''.join(map(str, a)))
        max_int = max(k, max_int)
    else:
        for i in range(l, n):
            a[l], a[i] = a[i], a[l]
            max_int = largest_int(arr, l + 1, max_int)
            a[l], a[i] = a[i], a[l] # backtrack

    return max_int

################################################################################
# Solution #2: sort using custom comparison
# O(n log n) time
def largest_int2(arr):
    #s = sorted(arr, key=cmp_to_key(comparator))
    s = sorted(arr, key=test_key)
    return int( ''.join([str(x) for x in s]) )


def comparator(x, y):
    xy = str(x) + str(y)
    yx = str(y) + str(x)
    
    return int(yx) - int(xy)

# https://docs.python.org/3/howto/sorting.html
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

# Code cmp_to_key(comparator) directly.
class test_key():
    def __init__(self, obj):
        self.obj = obj

    def __lt__(self, other):
        xy = str(self.obj) + str(other.obj)
        yx = str(other.obj) + str(self.obj)
        
        return int(yx) < int(xy)


################################################################################


arr = [1]
arr = [1, 2, 3]
arr = [10, 7, 76, 415]

print("\nlist of numbers = {}".format(arr))

#arr = [str(x) for x in arr]
#arr = list(map(str, arr))

n = largest_int(arr)
print("\nlargest int (sol #1) = {}".format(n))

n2 = largest_int2(arr)
print("\nlargest int (sol #2) = {}".format(n2))


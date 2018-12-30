'''
dcp#40

This problem was asked by Google.

Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
'''

'''
References:
https://stackoverflow.com/questions/14100169/find-the-element-that-appears-once
https://www.quora.com/Given-an-integer-array-such-that-every-element-occurs-3-times-except-one-element-which-occurs-only-once-how-do-I-find-that-single-element-in-O-1-space-and-O-n-time-complexity
https://www.careercup.com/question?id=7902674

Notes:
- If O(1) constraint not there, could use hashmap with values being counts of occurence
- XOR is associative and commutative, so it doesn't matter the order that elements appear in array/list

'''


# don't like this solution
def get_unique_integer2(arr):
    ones = 0
    twos = 0
    #not_threes

    for x in arr:
        twos |= ones & x # add x to twos if it's already in ones
        ones ^= x # if x is in ones, remove it, else add it

        # convert common 1's in ones and twos to 0
        not_threes = ~(ones & twos)
        ones &= not_threes
        twos &= not_threes

    return ones

# prefer this solution
def get_unique_integer(arr):
    ones = 0
    twos = 0

    for x in arr:
        # ones ^ x : if x is in ones, remove it, else add it
        # (ones ^ x) & ~twos : let x stay in ones if it was added (wasn't in ones in the first place) and if it's not in twos
        ones = (ones ^ x) & ~twos

        # twos ^ x : if x is in twos, remove it, else add it
        # (twos ^ x) & ~ones : let x stay in twos if it was added (wasn't in twos in the first place) and if it's not in ones
        twos = (twos ^ x) & ~ones

    return ones

'''
cases (state of x at start of loop):
x not in ones or twos:  x gets added to ones; x remains out of twos
x in ones but not twos: x removed from ones; x added to twos
x in twos but not ones: x remains out of ones; x removed from twos
x in both ones and twos: x removed from ones; x removed from twos

state (in ones, in twos) before and after (start and end of each loop iteration)
(0, 0): (1, 0)
(1, 0): (0, 1)
(0, 1): (0, 0)
(1, 1): (0, 0)

closed loop: (0, 0) -> (1,0) -> (0, 1) -> (0, 0)
'''

'''
ones    ones^x  twos    ~twos   final
        0        0       1      0
        0        1       0      0   
        1        0       1      1
        1        1       0      0
'''



x1 = [6, 1, 3, 3, 3, 6, 6] # should return 1; sum=28, n=7
x2 = [13, 19, 13, 13] # should return 19; sum=58, n=4
x3 = [1,2,3,4,5,1,2,3,4,1,2,3,4] # should return 5; sum=35, n=13


print(f"x1: {get_unique_integer(x1)}")
print(f"x2: {get_unique_integer(x2)}")
print(f"x3: {get_unique_integer(x3)}")

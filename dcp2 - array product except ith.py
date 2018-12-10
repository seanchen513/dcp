'''
dcp#2

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

Notes:
- int() truncates decimals to integer
'''

########################################

from functools import reduce

lst = [2,3,5,6]

prod = reduce(lambda x,y: x*y, lst)
lst2 = []

for x in lst:
    lst2.append(int(prod / x))

print(lst2)

########################################

# what if division is not available?

lst3 = []

for x in lst:
    s = 1
    for y in lst:
        if x != y:
            s *= y 
    lst3.append(s)

print(lst3)






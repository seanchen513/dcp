'''
dcp#74

This problem was asked by Apple.

Suppose you have a multiplication table that is N by N. That is, a 2D array where the value
at the i-th row and j-th column is (i + 1) * (j + 1) (if 0-indexed) or i * j (if 1-indexed).

Given integers N and X, write a function that returns the number of times X appears as a value 
in an N by N multiplication table.

For example, given N = 6 and X = 12, you should return 4, since the multiplication table looks like this:

| 1 | 2 | 3 | 4 | 5 | 6 |

| 2 | 4 | 6 | 8 | 10 | 12 |

| 3 | 6 | 9 | 12 | 15 | 18 |

| 4 | 8 | 12 | 16 | 20 | 24 |

| 5 | 10 | 15 | 20 | 25 | 30 |

| 6 | 12 | 18 | 24 | 30 | 36 |

And there are 4 12's in the table.
'''


# number of times that integer x appears as value in n-by-n multiplication table
# O(n^2)
def f(n, x):
    count = 0

    for i in range(1, n+1):
        for j in range(1, n+1):
            if x == i * j:
                count += 1

    return count


# mathematical solution: number of divisors of x in range 1..n
# O(n)
# note: other ways to tell if d is integer:
# - if d % 1 == 0
# - if d == int(d)
def f2(n, x):
    count = 0

    for i in range(1, n+1):
        d = x / i
        if (d.is_integer()) and (d <= n): 
            count += 1
    
    return count

################################################################################

x = 12
print ("x = ", x)
print("n   f1   f2")
for n in range(1, x+1):
    print("{:3d} {:3d} {:3d}".format(n, f(n, x), f2(n, x)))
    
#print(f(n=6, x=12)) # 4
#print(f2(n=6, x=12)) # 4



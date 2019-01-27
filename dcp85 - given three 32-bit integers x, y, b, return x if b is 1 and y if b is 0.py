"""
dcp#85

This problem was asked by Facebook.

Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0, using only mathematical or bit operations. You can assume b can only be 1 or 0.


"""

# Solution #1: mathematical way
def branch(x, y, b):
    return b * y + (1 - b) * x

# Solution #2: bits way
# ???


x = 513
y = 1037
b = 0

print("x = {}".format(x))
print("y = {}".format(y))

result = branch(x, y, b=0)
print("if b is 0, we get {}".format(result))

result = branch(x, y, b=1)
print("if b is 1, we get {}".format(result))




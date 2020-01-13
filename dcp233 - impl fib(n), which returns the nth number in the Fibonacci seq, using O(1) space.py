"""
dcp#233

This problem was asked by Apple.

Implement the function fib(n), which returns the nth number in the Fibonacci sequence, using only O(1) space.
"""

# Cannot use recursion, since call stack will use more than O(1) space.

# Assume n is positive integer.
def fib(n):
    if n in {1, 2}:
        return 1

    a = 1
    b = 1
    for _ in range(3, n):
        a, b = b, a + b
        
    return b


for n in range(1, 20):
    print("{:2}: {}".format(n, fib(n)))



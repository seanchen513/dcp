"""
dcp#129

Given a real number n, find the square root of n. For example, given n = 9, return 3.
"""

# Note: Newton's method does not work here.
# Sequence of estimations oscillates between two values for f(x) = sqrt(x).
# For f(x) = |x|^a where 0 < a < 1/2, sequence diverges.



# Solution using simple bisection.
# "error = 0.001 = 1e-3" means 0.1% error
def sqrt(n, error = 1e-12):
    if n < 0:
        return None

    if n == 0:
        return 0

    reciprocal = False
    if n < 1:
        n = 1 / n
        reciprocal = True

    k = n / 2
    err = k*k / n - 1
    step = 1
    while abs(err) > error:
        step += 1

        if err > 0:
            k = k - n / (2**step)
        else:
            k = k + n / (2**step) 

        err = (k * k / n) - 1

    if reciprocal:
        k = 1 / k

    return k


n = 9
n = 2
n = 0
n = 1
n = 0.5
n = 1e-12
n = 3.14159
n = 3.14159e-12

s = sqrt(n)
print("sqrt({}) = {}".format(n, s))
print("check: sqrt*sqrt = {}".format(s*s))

sqrt_n = n**0.5
err_s = (s - sqrt_n) / sqrt_n
err_n = (s * s - n) / n
print("error in s = {}".format(err_s))
print("error in s*s = {}".format(err_n))


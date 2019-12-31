"""
dcp#129

Given a real number n, find the square root of n. For example, given n = 9, return 3.
"""

"""
Note: Newton's method does not work here.
Sequence of estimations oscillates between two values for f(x) = sqrt(x).
For f(x) = |x|^a where 0 < a < 1/2, sequence diverges.
"""

# Solution using simple bisection, repeated.
# Here, error is defined as: (k*k - n) - 1
# where k is calculated square root of n so far.
# "error = 0.001 = 1e-3" means 0.1% error
def sqrt(n, error = 1e-12):
    if n < 0:
        return None

    if n == 0:
        return 0

    # if given n < 1, work with reciprocal, and then take reciprocal again at end
    reciprocal = False
    if n < 1:
        n = 1 / n
        reciprocal = True

    k = n / 2 # initial guess
    err = k*k / n - 1 # our definition of error
    
    #step = 1 # step number in repeated bisection
    step_power = 2.0

    while abs(err) > error:
        #step += 1
        step_power *= 2.0

        if err > 0:
            #k = k - n / (2**step)
            k -= n / step_power
        else: # err < 0, can't be 0 due to while condition
            #k = k + n / (2**step) 
            k += n / step_power 

        err = (k*k / n) - 1

    if reciprocal:
        k = 1 / k

    return k

###############################################################################

n = -1
n = 9
n = 2
n = 0
n = 1
n = 0.5
n = 1e-12
n = 3.14159265
n = 3.14159265e24
n = 3.14159265e-24

error = 1e-12

s = sqrt(n, error)

print("\nn = {}".format(n))
print("error = {}".format(error))

print("\nsqrt(n) = {}".format(s))
if s is None:
    exit()

print("check: sqrt*sqrt = {}".format(s*s))

sqrt_n = n**0.5
err_s = (s - sqrt_n) / sqrt_n
err_n = (s*s - n) / n

print("\ndifference in s (vs n**0.5) = {:.4}".format(s - sqrt_n))
print("difference in s*s (vs given n)= {:.4}".format(s*s - n))

print("\nerror in s (vs n**0.5) = {:.4}".format(err_s))
print("error in s*s (vs given n)= {:.4}".format(err_n))


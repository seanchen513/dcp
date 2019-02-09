"""
dcp#14

This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.

"""



import random


def mc_pi():
    sum = 0

    for n in range(1, 1000000):
        x = random.random()
        y = random.random()

        if x**2 + y**2 < 1.0:
            sum += 1

    return sum * 4.0 / 1000000


pi = mc_pi()
print("estimate of pi = {}".format(pi))




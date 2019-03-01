"""
dcp#66

This problem was asked by Square.

Assume you have access to a function toss_biased() which returns 0 or 1 with a probability that's not 50-50 (but also not 0-100 or 100-0). You do not know the bias of the coin.

Write a function to simulate an unbiased coin toss.
"""

import random

BIAS = 0.6 # number strictly between 0 and 1

def biased_coin():
    if random.random() > BIAS:
        return 1
    else:
        return 0


def unbiased_coin():
    toss1 = biased_coin()
    toss2 = biased_coin()

    if (toss1 and not toss2):
        return 0

    if (toss2 and not toss1):
        return 1

    return unbiased_coin()


count = 0
total = 1000000

for i in range(0, total):
    count += unbiased_coin()

print("{} / {} = {}".format(count, total, count/total))

# Var(X_i) = E(X_i ^2) - E(X_i)^2 = 1/2 - 1/4 = 1/4
# Var(X_1 + ... + X_n) = n * Var(X_i) = n / 4
# stddev = sqrt(Var) = sqrt(n) / 2
stddev = (count**0.5) / 2
print("stddev = {}".format(stddev))

dev = count - (total / 2)
print("dev = {}".format(dev))
print("dev / stddev = {}".format(dev/stddev))


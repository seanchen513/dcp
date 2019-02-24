"""
dcp#15

This problem was asked by Facebook.

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.

"""

# Would need some clarification on this problem.


import random

def pick_random_elt(stream):
    picked = None

    for i, e in enumerate(stream):
        if i == 0:
            picked = e
        elif random.randint(1, i+1) == 1:
            picked = e
    
    return picked


# simulate a stream for testing
stream = range(1000000)
#stream = range(10)

k = pick_random_elt(stream)
print("Random element picked = {}".format(k))


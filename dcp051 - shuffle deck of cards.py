"""
dcp051 - shuffle a deck of cards

This problem was asked by Facebook.

Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.
"""

import random


# Fisher-Yates modern shuffle
def shuffle(arr):
    n = len(arr) - 1

    for k in range(n, -1, -1):
        r = random.randint(0, k)
        arr[k], arr[r] = arr[r], arr[k]

    return arr

# can also loop in other direction
def shuffle2(arr):
    n = len(arr) - 1

    for k in range(0, n):
        r = random.randint(k, n-1)
        arr[k], arr[r] = arr[r], arr[k]

    return arr


deck = list(range(52))
print("deck = {}".format(deck))

shuffle2(deck)
print("\nshuffled deck = {}".format(deck))


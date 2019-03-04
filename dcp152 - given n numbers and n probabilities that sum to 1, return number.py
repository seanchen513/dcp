"""
dcp#152

This problem was asked by Triplebyte.

You are given n numbers as well as n probabilities that sum up to 1. Write a function to generate one of the numbers with its corresponding probability.

For example, given the numbers [1, 2, 3, 4] and probabilities [0.1, 0.5, 0.2, 0.2], your function should return 1 10% of the time, 2 50% of the time, and 3 and 4 20% of the time.

You can generate random numbers between 0 and 1 uniformly.
"""

import random

def pick_num(numbers, probs):
    r = random.random()
    
    cumul_prob = 0

    for index, p in enumerate(probs):
        cumul_prob += p
        if cumul_prob > r:
            return numbers[index]

def test(numbers, probs, sample_size):
    results = {}

    for n in numbers:
        results[n] = 0

    for _ in range(0, sample_size):
        results[pick_num(numbers, probs)] += 1

    return results


numbers = [1, 2, 3, 4]
probs = [0.1, 0.5, 0.2, 0.2]

num = pick_num(numbers, probs) 

print("numbers: {}".format(numbers))
print("probabilities: {}".format(probs))
print("number chosen: {}".format(num))

sample_size = 10000
results = test(numbers, probs, sample_size)
print("\nresults over {} calls:".format(sample_size))
print(results)


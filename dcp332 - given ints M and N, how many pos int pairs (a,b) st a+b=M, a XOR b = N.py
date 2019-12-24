"""
dcp#332

This problem was asked by Jane Street.

Given integers M and N, write a program that counts how many positive integer pairs (a, b) satisfy the following conditions:

a + b = M
a XOR b = N

"""


def find_pairs(m, n):
    sol = []

    for a in range(1, m):
        b = m - a

        if a ^ b == n:
            sol.append((a, b))

    return sol


m = 2**10 + 2**7 + 2**3
n = 2**3

m = 8
n = 4

sol = find_pairs(m, n)

print("\nm, n = {}, {}".format(m, n))
print("\nSolutions:\n{}".format(sol))

print("\nNumber of solutions = {}".format(len(sol)))


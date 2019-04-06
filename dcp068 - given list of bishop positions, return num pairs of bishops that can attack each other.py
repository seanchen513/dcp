"""
dcp#68

This problem was asked by Google.

On our special chessboard, two bishops attack each other if they share the same diagonal. This includes bishops that have another bishop located between them, i.e. bishops can attack through pieces.

You are given N bishops, represented as (row, column) tuples on a M by M chessboard. Write a function to count the number of pairs of bishops that attack each other. The ordering of the pair doesn't matter: (1, 2) is considered the same as (2, 1).

For example, given M = 5 and the list of bishops:

(0, 0)
(1, 2)
(2, 2)
(4, 0)
The board would look like this:

[b 0 0 0 0]
[0 0 b 0 0]
[0 0 b 0 0]
[0 0 0 0 0]
[b 0 0 0 0]

You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and 4.
"""

# Suppose bishop 1 has coords (x1, y1), and bishop 2 has coords (x2, y2).
# Then they can attack each other if and only if |x1 - x2| = |y1 - y2|

# Solution #1: check each pair of bishops once
# O(n^2) where n = # bishops
# Note how "m" is not used here
def num_bishop_pairs_attack(m, bishops):
    count = 0

    for i in range(0, len(bishops)):
        x_i = bishops[i][0]
        y_i = bishops[i][1]

        for j in range(i + 1, len(bishops)):
            dx = bishops[j][0] - x_i
            dy = bishops[j][1] - y_i

            if (dx == dy) or (dx == -dy):
                count += 1

    return count


# Solution #2: count # bishops along each diagonal
# There are 2m-1 diagonals with slope 1, and another 2m-1 with slope -1, for total of 4m-2.
# Actually, we don't care about the 4 diagonals of size one; so total is 4m-6.
# If there are k bishops in the same diagonal, then there are kC2 = k*(k-1)/2
# pairs of bishops in that diagonal that can attack each other.
#
# O(m) time
def num_bishop_pairs_attack2(m, bishops):
    counts_pos = {}
    counts_neg = {}

    for b in bishops:
        x = b[0]
        y = b[1]

        # for cells in same diagonal of slope +1, x + y == constant (0, ..., 2m-2)
        if x + y in counts_pos:
            counts_pos[x+y] += 1
        else:
            counts_pos[x+y] = 1

        # for cells in same diagonal of slope -1, x - y == constant (-m+1, ..., m-1)
        if x - y in counts_neg:
            counts_neg[x-y] += 1
        else:
            counts_neg[x-y] = 1

    total = 0

    for _, count in counts_pos.items():
        total += count*(count - 1)/2

    for _, count in counts_neg.items():
        total += count*(count - 1)/2

    return int(total)


def print_board(m, bishops):
    bishops.sort()

    for r in range(0, m):
        for c in range(0, m):
            if (r, c) in bishops:
                print("b", end=" ")
            else:
                print("0", end=" ")
            
        print()


# This comes from a solution for the max bishops that can be placed on 8x8 chessboard
# so that no bishops can attack each other.
# Solution should be 0.
m = 8
bishops = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
    (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6)]

# from problem statement
m = 5
bishops = [(0, 0), (1, 2), (2, 2), (4, 0)]


k = num_bishop_pairs_attack(m, bishops)
k2 = num_bishop_pairs_attack2(m, bishops)

print_board(m, bishops)

print("\nNumber of pairs of bishops that can attack each other (method 1): {}".format(k))
print("\nNumber of pairs of bishops that can attack each other (method 2): {}".format(k2))



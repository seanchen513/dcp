"""
dcp#376 (easy)

This problem was asked by Google.

You are writing an AI for a 2D map game. You are somewhere in a 2D grid, and there are coins strewn about over the map.

Given the position of all the coins and your current position, find the closest coin to you in terms of Manhattan distance. That is, you can move around up, down, left, and right, but not diagonally. If there are multiple possible closest coins, return any of them.

For example, given the following map, where you are x, coins are o, and empty spaces are . (top left is 0, 0):

---------------------
| . | . | x | . | o |
---------------------
| o | . | . | . | . |
---------------------
| o | . | . | . | o |
---------------------
| . | . | o | . | . |
---------------------
return (0, 4), since that coin is closest. This map would be represented in our question as:

Our position: (0, 2)
Coins: [(0, 4), (1, 0), (2, 0), (3, 2)]
"""

from functools import cmp_to_key

# Assume coins is not empty
def closest_coin(x, coins):
    min_dist = abs(x[0] - coins[0][0]) + abs(x[1] - coins[0][1])
    min_coin = coins[0]

    for i in range(1, len(coins)):
        d = abs(x[0] - coins[i][0]) + abs(x[1] - coins[i][1])

        if d < min_dist:
            min_dist = d
            min_coin = coins[i]

    return min_coin


# not needed to solve original problem
# used for sorting list by Manhattan distance with respect to given point "pos"
def manhattan_dist_wrt(pos):
    def manhattan_dist(p1, p2):
        return abs(p1[0] - pos[0]) + abs(p1[1] - pos[1]) \
            - abs(p2[0] - pos[0]) - abs(p2[1] - pos[1])

    return manhattan_dist


# assume coordinates are >= 0
def print_grid(coins, pos):
    unzipped = list(zip(*coins))
    max_x = max(max(unzipped[0]), pos[0])
    max_y = max(max(unzipped[1]), pos[1])

    for x in range(max_x + 1):
        for y in range(max_y + 1):
            if (x, y) == pos:
                print("X", end = " ")
            elif (x, y) in coins:
                print("O", end = " ")
            else:
                print(".", end = " ")

        print()


coins = [(0, 4), (1, 0), (2, 0), (3, 2)]
pos = (0, 2)

min_coin = closest_coin(pos, coins)

print("coins = {}".format(coins))
print("pos = {}\n".format(pos))

print_grid(coins, pos)

print("\nclosest coin = {}".format(min_coin))

s = sorted(coins, key=cmp_to_key(manhattan_dist_wrt(pos)))
print("sorted by Manhattan distance = {}".format(s))


"""
dcp#392

This problem was asked by Google.

You are given a 2D matrix of 1s and 0s where 1 represents land and 0 represents water.

Grid cells are connected horizontally orvertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

An island is a group is cells connected horizontally or vertically, but not diagonally. There is guaranteed to be exactly one island in this grid, and the island doesn't have water inside that isn't connected to the water around the island. Each cell has a side length of 1.

Determine the perimeter of this island.

For example, given the following matrix:

[[0, 1, 1, 0],
[1, 1, 1, 0],
[0, 1, 1, 0],
[0, 0, 1, 0]]
Return 14.
"""

# Solution #1: cell-by-cell approach
# Assume "arr" is rectangular grid.
def find_perimeter(arr):
    n_rows = len(arr)
    n_cols = len(arr[0])

    p = 0

    for x in range(n_rows):
        for y in range(n_cols):
            if arr[x][y] == 1:
                if (x - 1 < 0) or (arr[x-1][y] == 0):
                    p += 1
                if (y - 1 < 0) or (arr[x][y-1] == 0):
                    p += 1
                if (x + 1 >= n_cols) or (arr[x+1][y] == 0):
                    p += 1
                if (y + 1 >= n_rows) or (arr[x][y+1] == 0):
                    p += 1

    return p


# Solution #2
# Count 1s on border of grid, and transitions 0->1 and 1->0 within grid.
def find_perimeter2(arr):
    n_rows = len(arr)
    n_cols = len(arr[0])

    p = sum(arr[0]) + sum(arr[n_rows - 1])

    for r in range(n_rows):
        p += arr[r][0] + arr[r][n_cols - 1]

    # count vertical transitions
    for r in range(n_rows - 1):
        for c in range(n_cols):
            if arr[r][c] != arr[r+1][c]:
                p += 1

    # count horizontal transitions
    for r in range(n_rows):
        for c in range(n_cols - 1):
            if arr[r][c] != arr[r][c+1]:
                p += 1

    return p


def print_grid(arr):
    for r in arr:
        for c in r:
            print(c, end=" ")
        print()


arr = [
    [0, 1, 1, 0],
    [1, 1, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0]]


print_grid(arr)

p = find_perimeter(arr)
p2 = find_perimeter2(arr)

print("\nperimeter (sol#1) = {}".format(p))
print("\nperimeter (sol#2) = {}".format(p2))


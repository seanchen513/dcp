"""
dcp#84

This problem was asked by Amazon.

Given a matrix of 1s and 0s, return the number of "islands" in the matrix. A 1 represents land and 0 represents water, so an island is a group of 1s that are neighboring and their perimiter is surrounded by water.

For example, this matrix has 4 islands.

1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1

"""

import pprint as pprint

def island_sizes_util(matrix, n_rows, n_cols, i, j, visited):
    if (i not in range(n_rows)) or (j not in range(n_cols)):
        return 0

    if (matrix[i][j] == 0) or visited[i][j]:
        return 0

    visited[i][j] = 1

    return (1 + island_sizes_util(matrix, n_rows, n_cols, i+1, j, visited)
        + island_sizes_util(matrix, n_rows, n_cols, i, j+1, visited)
        + island_sizes_util(matrix, n_rows, n_cols, i-1, j, visited)
        + island_sizes_util(matrix, n_rows, n_cols, i, j-1, visited))

# alternate util method to have fewer recursive calls
def island_sizes_util2(matrix, n_rows, n_cols, i, j, visited):
    if (matrix[i][j] == 0) or visited[i][j]:
        return 0

    visited[i][j] = 1

    n = 1

    if i + 1 < n_rows:
        n += island_sizes_util2(matrix, n_rows, n_cols, i+1, j, visited)
    if i - 1 >= 0:
        n += island_sizes_util2(matrix, n_rows, n_cols, i-1, j, visited)
    if j + 1 < n_cols:
        n += island_sizes_util2(matrix, n_rows, n_cols, i, j+1, visited)
    if j - 1 >= 0:
        n += island_sizes_util2(matrix, n_rows, n_cols, i, j-1, visited)

    return n

def island_sizes(matrix):
    n_rows = len(matrix)
    n_cols = len(matrix[0])

    visited = [[0] * n_cols for _ in range(n_rows)]
    island_sizes = []

    for i in range(n_rows):
        for j in range(n_cols):
            if (matrix[i][j] == 0) or visited[i][j]:
                continue
            
            #island_size = island_sizes_util(matrix, n_rows, n_cols, i, j, visited)
            island_size = island_sizes_util2(matrix, n_rows, n_cols, i, j, visited)
            island_sizes.append(island_size)
            
    return island_sizes


m = [[1,0,1,0,1]
    ]

m = [
    [1,0,0,0,0],
    [0,0,1,1,0],
    [0,1,1,0,0],
    [0,0,0,0,0],
    [1,1,0,0,1],
    [1,1,0,0,1]
    ]


pprint.pprint(m)

sizes = island_sizes(m)
print("\nisland sizes = {}".format(sizes))

n = len(sizes)
print("\nnumber of islands = {}".format(n))


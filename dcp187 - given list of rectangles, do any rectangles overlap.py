"""
dcp#187

This problem was asked by Google.

You are given given a list of rectangles represented by min and max x- and y-coordinates. Compute whether or not a pair of rectangles overlap each other. If one rectangle completely covers another, it is considered overlapping.

For example, given the following rectangles:

{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
},
{
    "top_left": (-1, 3),
    "dimensions": (2, 1)
},
{
    "top_left": (0, 5),
    "dimensions": (4, 3)
}

return true as the first and third rectangle overlap each other.
"""

from pprint import pprint

def area_intersection(r1, r2):
    xmin = max(r1["xmin"], r2["xmin"])
    xmax = min(r1["xmax"], r2["xmax"])

    ymin = max(r1["ymin"], r2["ymin"])
    ymax = min(r1["ymax"], r2["ymax"])

    if (xmin >= xmax) or (ymin >= ymax):
        return 0
    else:
        return (xmax - xmin) * (ymax - ymin)


def convert_rectangles(rectangles):
    rectangles_converted = []

    for r in rectangles:
        d = {}
        d["xmin"] = r["top_left"][0]
        d["xmax"] = d["xmin"] + r["dimensions"][0]
        
        d["ymax"] = r["top_left"][1]
        d["ymin"] = d["ymax"] - r["dimensions"][1]

        rectangles_converted.append(d)

    return rectangles_converted


# Returns matrix of areas of intersections for each pair of rectangles...
# Argument "rectangles" in the converted format
def intersect_matrix(rectangles):
    n = len(rectangles)
    matrix = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(i, n):
            matrix[i][j] = area_intersection(rectangles[i], rectangles[j])
            matrix[j][i] = matrix[i][j] # matrix must be symmetric

    return matrix


rectangles = [
    {
        "top_left": (1, 4),
        "dimensions": (3, 3) # width, height
    },
    {
        "top_left": (-1, 3),
        "dimensions": (2, 1)
    },
    {
        "top_left": (0, 5),
        "dimensions": (4, 3)
    }]


print("\nRectangles:")
pprint(rectangles)

rectangles_converted = convert_rectangles(rectangles)

print("\nConverted:")
pprint(rectangles_converted)

print("\nMatrix of areas of intersections:")
matrix = intersect_matrix(rectangles_converted)
pprint(matrix)


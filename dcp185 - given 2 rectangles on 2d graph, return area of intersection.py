"""
dcp#185
dip#122 (12/9/19)

This problem was asked by Google.

Given two rectangles on a 2D graph, return the area of their intersection. If the rectangles don't intersect, return 0.

For example, given the following rectangles:

{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
}

and

{
    "top_left": (0, 5),
    "dimensions": (4, 3) # width, height
}
return 6.
"""


def area_intersection(r1, r2):
    # rectangle 1
    r1_xmin = r1["top_left"][0]
    r1_xmax = r1_xmin + r1["dimensions"][0]
    
    r1_ymax = r1["top_left"][1]
    r1_ymin = r1_ymax - r1["dimensions"][1]

    # rectangle 2
    r2_xmin = r2["top_left"][0]
    r2_xmax = r2_xmin + r2["dimensions"][0]
    
    r2_ymax = r2["top_left"][1]
    r2_ymin = r2_ymax - r2["dimensions"][1]

    # intersection
    xmin = max(r1_xmin, r2_xmin)
    xmax = min(r1_xmax, r2_xmax)

    ymin = max(r1_ymin, r2_ymin)
    ymax = min(r1_ymax, r2_ymax)

    if (xmin >= xmax) or (ymin >= ymax):
        return 0
    else:
        return (xmax - xmin) * (ymax - ymin)


r1 = {
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
}

r2 = {
    "top_left": (0, 5),
    "dimensions": (4, 3) # width, height
}

a = area_intersection(r1, r2)

print("area of intersection = {}".format(a))

"""
other cases:
- non-intersecting (and not touching)
- touching on a side
    - horizontally, vertically
    - partial or complete intersection of side
- touching just at a corner
- one rectangle entirely inside the other rectangle...

"""


"""
dcp#340

This problem was asked by Google.

Given a set of points (x, y) on a 2D cartesian plane, find the two closest points. For example, given the points [(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)], return [(-1, -1), (1, 1)].
"""

import math


# O(n^2)
def closest_points(points):
    n = len(points)
    min_d2 = 2**31 # minimum distance found so far
    
    # keep track of points that are closest so far
    p1 = None
    p2 = None 

    for i in range(n):
        x = points[i][0]
        y = points[i][1]

        for j in range(i + 1, n):
            d2 = (x - points[j][0])**2 + (y - points[j][1])**2
        
            if  d2 < min_d2:
                min_d2 = d2
                p1 = i
                p2 = j

    return min_d2, [points[p1], points[p2]]


points = [(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)] # [(-1, -1), (1, 1)]

min_d2, pts = closest_points(points)

print("\npoints = {}".format(points))
print("\nclosest points = {}".format(pts))
print("\nclosest distance = {}".format(math.sqrt(min_d2)))


"""
dcp#150

This problem was asked by LinkedIn.

Given a list of points, a central point, and an integer k, find the nearest k points from the central point.

For example, given the list of points [(0, 0), (5, 4), (3, 1)], the central point (1, 2), and k = 2, return [(0, 0), (3, 1)].
"""

# Clarify that we are using Euclidean distance, and that we are working only in 2d.
# Need to clarify what to do in case of ties.
# Can use queue, or put distances in list and sort.

def find_nearest_points(points, central_point, k):
    # Don't need a dict here; a list also works.
    ds = {} # dictionary of points and their distances to central point
    x = central_point[0]
    y = central_point[0]

    for pt in points:
       ds[pt] = (pt[0] - x)**2 + (pt[1] - y)**2

    lst = sorted(ds.items(), key=lambda kv: kv[1]) # sort by values in dict ds

    #return lst[:k] # if we want list of tuples (point, dist^2)
    return [tup[0] for tup in lst[:k]]


points = [(0, 0), (5, 4), (3, 1)]
central_point = (1, 2)
k = 2

nearest_points = find_nearest_points(points, central_point, k)

print("\npoints:")
print(points)

print("\ncentral point = {}".format(central_point))
print("k = {}".format(k))

print("\nnearest k points:")
print(nearest_points)


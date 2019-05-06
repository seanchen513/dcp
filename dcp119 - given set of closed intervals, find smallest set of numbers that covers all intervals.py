"""
dcp#119

This problem was asked by Google.

Given a set of closed intervals, find the smallest set of numbers that covers all the intervals. If there are multiple smallest sets, return any of them.

For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], one set of numbers that covers all these intervals is {3, 6}.

//
dcp#200

This problem was asked by Microsoft.

Let X be a set of n intervals on the real line. We say that a set of points P "stabs" X if every interval in X contains at least one point in P. Compute the smallest set of points that stabs X.

For example, given the intervals [(1, 4), (4, 5), (7, 9), (9, 12)], you should return [4, 9].
"""

# Assume intervals are closed.


# O(n log n) time due to sorting, where n = number of intervals
def find_cover(intervals):
    # sort by right endpoint
    intervals.sort(key=lambda intvl: intvl[1])

    point = intervals[0][1]
    cover = [point]

    for i in range(1, len(intervals)):
        if point >= intervals[i][0] and point <= intervals[i][1]:
            continue

        point = intervals[i][1]
        cover.append(point)

    return cover


intervals = [ [0, 1] ] # trivial example

# telescoping intervals
intervals = [ [0,4], [0,3], [0,2], [0,1] ] # possible covers [0], ..., [1]
intervals = [ [0,7], [1,6], [2,5], [3,4] ] # possible covers = [3], ..., [4]

intervals = [ [0, 3], [2, 6], [3, 4], [6, 9] ] # dcp119; possible covers = [3, 6], ..., [3, 9]
intervals = [ [1, 4], [4, 5], [7, 9], [9, 12] ] # dcp200; [4, 9]

print("\nintervals = {}".format(intervals))

cover = find_cover(intervals)
print("\ncover (points) = {}".format(cover))


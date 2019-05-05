"""
dcp#191

This problem was asked by Stripe.

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Intervals can "touch", such as [0, 1] and [1, 2], but they won't be considered overlapping.

For example, given the intervals (7, 9), (2, 4), (5, 8), return 1 as the last interval can be removed and the first two won't overlap.

The intervals are not necessarily sorted in any order.
"""

# Since "touching" intervals aren't considered overlapping, we can assume all intervals are closed.
# We represent intervals as lists of 2 elements.
# Could define a simple Interval class to make code a bit more readable.


# Sort array by first endpoint of each interval.
# Iterate through array and keep track of smallest right endpoint of current overlapping intervals.
# Current set of overlapping intervals terminates when next interval doesn't overlap with smallest right endpoint.
# Delete all intervals of current overlapping intervals except the one with smallest right endpoint.
# O(n log n) time determined by sorting.
def find_num_intervals_to_remove(intervals):
    intervals.sort()
    #print("sorted intervals: {}".format(intervals))
    
    min_right_endpoint = intervals[0][1]
    count_to_delete = 0

    for i in range(1, len(intervals)):
        if intervals[i][0] < min_right_endpoint: # overlap
            min_right_endpoint = min(min_right_endpoint, intervals[i][1])
            count_to_delete += 1
        else:
            min_right_endpoint = intervals[i][1]

    return count_to_delete




intervals = [(7, 9), (2, 4), (5, 8)] # 1
#intervals = [ [1,2], [2,3], [3,4], [1,3] ] # 1
#intervals = [ [1,2], [1,2], [1,2] ] # 2
#intervals = [ [1,2], [2,3] ] # 0

n = find_num_intervals_to_remove(intervals)

print("intervals: {}".format(intervals))
print("min number of intervals to remove to make rest non-overlapping = {}".format(n))


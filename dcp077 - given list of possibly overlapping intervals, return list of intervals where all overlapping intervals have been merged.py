"""
dcp#77

This problem was asked by Snapchat.

Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].
"""

# Ignore difference between open and closed intervals.
# Represent intervals as lists of endpoints (since tuples are immutable).


# in-place
# O(n log n) time due to sorting; merge step is O(n)
# O(1) extra space
def merge_intervals_inplace(intervals):
    #intervals.sort(key=lambda intvl: intvl[0])
    intervals.sort() # in-place sort
    
    index = 0 # tracks previous interval of merged intervals

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[index][1]: # overlap
            # merge them
            intervals[index][1] = max( intervals[index][1], intervals[i][1] )
        else:
            intervals[index + 1] = intervals[i]
            index += 1

    # remove extraneous intervals
    for i in range(index + 1, len(intervals)):
        intervals.pop()

    return intervals



intervals = [ [1, 3], [5, 8], [4, 10], [20, 25] ] # [ [1, 3], [4, 10], [20, 25] ]
#intervals =  [ [1, 3], [2, 4], [5, 7], [6, 8] ] # [ [1, 4], [5, 8]]

print("\nintervals = {}".format(intervals))

merge_intervals_inplace(intervals)
print("\nmerged intervals = {}".format(intervals))


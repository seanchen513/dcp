"""
dcp#21

This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""

# Since "touching" intervals aren't considered overlapping, we can assume all intervals are closed.
# We represent intervals as lists of 2 elements.
# Could define a simple Interval class to make code a bit more readable.

# To clarify: what to do about an interval that ends exactly when another starts?

# Combine start times and end times of all arrays into a single array, then sort it.
# Iterate through array, incrementing a counter for each start time,
# and decrementing the counter for each end time.  The max of the
# counter is the min number of rooms required.
# O(n log n) time determined by sorting.
def min_rooms(intervals):
    times = []
    for intvl in intervals:
        times.append((intvl[0], "start"))
        times.append((intvl[1], "end"))

    # Here, if a start time is equal to an end time, the end time will be processed first
    # since "end" < "start".  The corresponding intervals can use the same room.

    times.sort()
    print("sorted times: {}".format(times))
    
    count = 0
    max_count = 0

    for t in times:
        if t[1] == "start":
            count += 1
            max_count = max(max_count, count)
        else:
            count -= 1

    return max_count


intervals = [ [1, 2] ] # 1
intervals = [ [1, 2], [1, 2], [1, 2] ] # 3
intervals = [ [1, 2], [2, 3] ] # 1
intervals = [ [30, 75], [0, 50], [60, 150] ] # 2 

n = min_rooms(intervals)

print("intervals: {}".format(intervals))
print("min rooms needed = {}".format(n))


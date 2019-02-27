"""
dcp#144

This problem was asked by Google.

Given an array of numbers and an index i, return the index of the nearest larger number of the number at index i, where distance is measured in array indices.

For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.

If two distances to larger numbers are the equal, then return any one of them. If the array at i doesn't have a nearest larger integer, then return null.

Follow-up: If you can preprocess the array, can you do this in constant time?
"""

# Need clarification on preprocessing.
# Obviously, we could just calculate the answer for each index ahead of time, but thats "cheating".


def nearest_larger_int(arr, index):

    # how far the index can move in each direction before going out of bounds
    d_minus = index
    d_plus = len(arr) - index - 1

    for d in range(1, max(d_minus, d_plus) + 1):
        if d <= d_minus:
            if arr[index - d] > arr[index]:
                return index - d
        
        if d <= d_plus:
            if arr[index + d] > arr[index]:
                return index + d

    return None


arr = [4, 1, 3, 5, 6]
index = 0
n = nearest_larger_int(arr, index)

print("arr = {}".format(arr))
print("index = {}".format(index))
print("n = {}".format(n))

if n is not None:
    print("arr[n] = {}".format(arr[n]))


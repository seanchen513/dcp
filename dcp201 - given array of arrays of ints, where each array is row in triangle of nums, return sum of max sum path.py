"""
dcp#201

This problem was asked by Google.

You are given an array of arrays of integers, where each array corresponds to a row in a triangle of numbers. For example, [[1], [2, 3], [1, 5, 1]] represents the triangle:

  1
 2 3
1 5 1

We define a path in the triangle to start at the top and go down one row at a time to an adjacent value, eventually ending with an entry on the bottom row. For example, 1 -> 3 -> 5. The weight of the path is the sum of the entries.

Write a program that returns the weight of the maximum weight path.
"""

# To clarify: can integers be 0 or negative?
# How to get path of max weight?
# Iterative solution?

"""
How many paths are there? Suppose len(array) = n. There are n levels, and n elements in last level.
....
"""

# Recursive solution
def max_weight(arr, level=0, index=0, weight=0, max_wt=0):
    #print("level: {}, index: {}".format(level, index))
    weight += arr[level][index]
    
    if weight > max_wt:
        max_wt = weight

    if level == len(arr) - 1:
        return max_wt
    else:
        return max( max_weight(arr, level + 1, index, weight, max_wt), 
            max_weight(arr, level + 1, index + 1, weight, max_wt)
        )


arr = [[1]]
arr = [[1], [2, 3], [1, 5, 1]] 

print("\narray:\n{}".format(arr))

max_wt = max_weight(arr)
print("\nmax weight = {}".format(max_wt))


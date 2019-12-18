"""
dcp#377
LC#480
"Sliding Window Median"

This problem was asked by Microsoft.

Given an array of numbers arr and a window of size k, print out the median of each window of size k starting from the left and moving right by one position each time.

For example, given the following array and k = 3:

[-1, 5, 13, 8, 2, 3, 3, 1]
Your function should print out the following:

5 <- median of [-1, 5, 13]
8 <- median of [5, 13, 8]
8 <- median of [13, 8, 2]
3 <- median of [8, 2, 3]
3 <- median of [2, 3, 3]
3 <- median of [3, 3, 1]
Recall that the median of an even-sized list is the average of the two middle numbers.
"""

"""
For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
 """

from heapq import heapify, heappush, heappop

"""
Use 2 heaps that together store the k elements in the window.  
Max heap stores elements <= median, and min heap stores elements > median.
If k is odd, the median of the window is the top element of the max heap.
If k is even, the median is the average of the top elements of the two heaps.

Each time the window moves, remove the oldest element from whichever heap it's in,
and add the new element to the appropriate heap.
Keep sizes of heaps equal or so that maxheap has one more element than minheap.

Python's heapq uses a min heap.  Make a max heap by taking negatives of elements.

O(nk) since removing an element from a heap of size k is O(k).
"""

# Assume k is positive integer between 1 and len(arr).
# if k even, maxheap and minheap will have equal size
# if k odd, maxheap will have one more element than minheap

# after sorting:
# k even: eg, k=6, indices 0..5, median is avg of values at indices 2 and 3
# elements at 0, 1, 2 go to max heap; elements at 3, 4, 5 go to min heap  

# k odd: eg, k=7, indices 0..6, median is at index 3
# elements at 0, 1, 2, 3 go to max heap; elements at 4, 5, 6 go to min heap

def get_median(k, maxheap, minheap):
    if k % 2 == 0:
        median = (-maxheap[0] + minheap[0]) / 2
    else:
        median = -maxheap[0]

    print("median = {}".format(median))
    print("window = {}".format(arr[:k]))
    print("maxheap = {}".format(maxheap))
    print("minheap = {}\n".format(minheap))

    return median


def print_medians(arr, k):
    # create minheap from initial window
    minheap = arr[:k]
    heapify(minheap) # O(k)

    # move smaller half of elements from minheap to maxheap
    n = (k + 1) // 2 # max heap size
    maxheap = []
    for _ in range(n):
        heappush(maxheap, -heappop(minheap))

    median = get_median(k, maxheap, minheap)

    # eg, if len(arr) = 6 and k = 3, then i = 0..3 (last window is 3,4,5)
    for i in range(0, len(arr) - k):
        # remove oldest element from window
        if arr[i] <= median: 
            maxheap.remove(-arr[i]) # treat as list; O(k)
            heapify(maxheap) # O(k)
        else:
            minheap.remove(arr[i]) # treat as list; O(k)
            heapify(minheap) # O(k)

        # add new element to window
        if arr[i + k] <= median:
            heappush(maxheap, -arr[i + k]) # O(log k)
        else:
            heappush(minheap, arr[i + k]) # O(log k)

        # rebalance if needed
        if len(maxheap) > len(minheap) + 1:
            heappush(minheap, -heappop(maxheap))
        elif len(minheap) > len(maxheap):
            heappush(maxheap, -heappop(minheap))

        # calculate median for new window
        median = get_median(k, maxheap, minheap)


###############################################################################

arr = [-1, 5, 13, 8, 2, 3, 3, 1] # dcp377
arr = [1,3,-1,-3,5,3,6,7] # LC480
k = 3

print("original arr:\n{}".format(arr))
print("k = {}\n".format(k))
print("Sliding window medians:\n")
print_medians(arr, k)


"""
dcp#154

This problem was asked by Amazon.

Implement a stack API using only a heap. A stack implements the following methods:

    push(item), which adds an element to the stack
    pop(), which removes and returns the most recently added element (or throws an error if there is nothing on the stack)

Recall that a heap has the following operations:

    push(item), which adds a new key to the heap
    pop(), which removes and returns the max value of the heap

"""

# ask if we can use python's heapq module
# ask if it's ok if we use a minheap (which heapq implements)

import heapq

"""
heapq.heappush(heap, item)
Push the value item onto the heap, maintaining the heap invariant.

heapq.heappop(heap)
Pop and return the smallest item from the heap, maintaining the heap invariant. 
If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0].
"""

# implements stack from minheap
class StackFromHeap:
    def __init__(self):
        self.heap = []

        # use counter that gets decremented since we're using a minheap and want stack LIFO behavior
        self.negative_counter = 0

    def push(self, item):
        heapq.heappush(self.heap, (self.negative_counter, item))
        self.negative_counter -= 1

    def pop(self):
        try:
            heap_item = heapq.heappop(self.heap)
        except IndexError:
            return None # or should throw error as stated in problem statement

        return heap_item[1]



stack = StackFromHeap()

a = [1, 2, 3, 4, 5]

print("original list of items to be pushed into stack in order:")
print(a)

for x in a:
    stack.push(x)

print("\nitems popped from stack:")

x = stack.pop()
while x is not None:
    print(x)
    x = stack.pop()

# try to pop when stack is empty
x = stack.pop


"""
dcp#53

This problem was asked by Apple.

Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it.
"""

# Clarify: Can we use Python list with append() and pop() as a stack?

# IDEA: Push into queue by pushing into 1st stack.
# When need to pop from queue:
#       If 2nd stack is empty, pop elements from 1st stack and push into 2nd stack one at a time.
#       Pop from 2nd stack.

class QueueUsingStacks():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def empty(self):
        return (not self.stack1) and (not self.stack2)

    def enqueue(self, x):
        self.stack1.append(x)

    def dequeue(self):
        if self.empty():
            print("ERROR: queue is empty")
            return

        if self.stack2:
            return self.stack2.pop()
        else:
            while self.stack1:
                x = self.stack1.pop()
                self.stack2.append(x)

            return self.stack2.pop()


a = [1, 2, 3, 4, 5]

q = QueueUsingStacks()

for x in a:
    q.enqueue(x)

print("a = {}".format(a))

print("popping elements one at a time from queue:")

while not q.empty():
    x = q.dequeue()
    print(x)


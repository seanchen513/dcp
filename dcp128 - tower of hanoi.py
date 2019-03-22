"""
dcp#128

The Tower of Hanoi is a puzzle game with three rods and n disks, each a different size.

All the disks start off on the first rod in a stack. They are ordered by size, with the largest disk on the bottom and the smallest one at the top.

The goal of this puzzle is to move all the disks from the first rod to the last rod while following these rules:

    You can only move one disk at a time.
    A move consists of taking the uppermost disk from one of the stacks and placing it on top of another stack.
    You cannot place a larger disk on top of a smaller disk.

Write a function that prints out all the steps necessary to complete the Tower of Hanoi. You should assume that the rods are numbered, with the first rod being 1, the second (auxiliary) rod being 2, and the last (goal) rod being 3.

For example, with n = 3, we can do this in 7 moves:

Move 1 to 3
Move 1 to 2
Move 3 to 2
Move 1 to 3
Move 2 to 1
Move 2 to 3
Move 1 to 3
"""

"""
Since we're given solution for n = 3, a natural question is, Can we base a
solution for n = 4 on the solution for n = 3?

A   B   C
1
2
3
4

    1
    2
4   3   _
    
    1
    2
_   3   4

        1
        2
        3
_   _   4


General pattern for n disks:
1. Move n-1 disks from A to B. (from_rod to aux_rod)
2. Move nth disk from A to C. (from_rod to to_rod)
3. Move n-1 disks from B to C. (aux_rod to to_rod)

"""


def tower(n, from_rod, to_rod, aux_rod, step=[1]):
    if n == 1:
        print("{}. Move {} to {}".format(step[0], from_rod, to_rod))
        step[0] += 1
        return

    tower(n-1, from_rod, aux_rod, to_rod, step)

    # ok since all n-1 smaller disks are on aux_rod now
    print("{}. Move {} to {}".format(step[0], from_rod, to_rod)) 
    step[0] += 1

    tower(n-1, aux_rod, to_rod, from_rod, step)


n = 3 # 2**n - 1 moves required
#tower(n, "A", "C", "B")
tower(n, "1", "3", "2")


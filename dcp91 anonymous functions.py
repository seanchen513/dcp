"""
dcp#91

This problem was asked by Dropbox.

What does the below code snippet print out? How can we fix the anonymous functions to behave as we'd expect?

functions = []
for i in range(10):
    functions.append(lambda : i)

for f in functions:
    print(f())
"""

# Given code prints 9 ten times.
# Problem is closure property in Python.
# https://stackoverflow.com/questions/233673/how-do-lexical-closures-work
# Separate functions are defined, but they each have the closure of the environment
# that they're defined in.  In this env, variable i is mutated, and the closures
# all refer to the same i.


# solution #1
functions = []
for i in range(10):
    functions.append(lambda j, i=i: i)
    #functions.append(lambda j, i2=i: i2) # same effect

for f in functions:
    print(f(0))


# solution #2
functions2 = []
for k in range(10):
    def fng(n): # function generator
        def func(x): return n
        return func

    functions2.append(fng(k)) # invoke function generator instead

print()
for f in functions2:
    print(f(0))


"""
dcp#188

This problem was asked by Google.

What will this code print out?

def make_functions():
    flist = []

    for i in [1, 2, 3]:
        def print_i():
            print(i)
        flist.append(print_i)

    return flist

functions = make_functions()
for f in functions:
    f()
How can we make it print out what we apparently want?

"""


# prints out:
# 3
# 3
# 3
def make_functions():
    flist = []

    for i in [1, 2, 3]:
        def print_i():
            print(i)
        flist.append(print_i)

    return flist


# Solution #1: Return lambda in print_i()
# prints out:
# 1
# 2
# 3
def make_functions_fixed():
    flist = []
    
    def print_i(j):
        return lambda: print(j)

    for i in [1, 2, 3]:
        ### This also works.
        # def print_i(i):
        #     return lambda: print(i)
        flist.append(print_i(i))

    return flist


# Solution #2: Use lambda directly
def make_functions_fixed2():
    flist = []
    
    for i in [1, 2, 3]:
        flist.append(lambda i=i: print(i))

    return flist


# Solution #3: Use function generator
def make_functions_fixed3():
    flist = []
    
    def print_i_generator(j):
        def print_i():
            print(j)

        return print_i

    for i in [1, 2, 3]:
        flist.append(print_i_generator(i))

    return flist


print("\nOriginal:")
functions = make_functions()
for f in functions:
    f()

print("\nSoltuion #1 (return lambda in print_i()):")
functions = make_functions_fixed()
for f in functions:
    f()

print("\nSoltuion #2 (use lambda directly):")
functions = make_functions_fixed2()
for f in functions:
    f()

print("\nSoltuion #3 (use function generator):")
functions = make_functions_fixed2()
for f in functions:
    f()


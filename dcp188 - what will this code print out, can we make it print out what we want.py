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


print("\nOriginal:")
functions = make_functions()
for f in functions:
    f()

print("\nFixed:")
functions = make_functions_fixed()

for f in functions:
    f()


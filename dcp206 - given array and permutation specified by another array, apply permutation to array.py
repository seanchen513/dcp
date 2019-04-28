"""
dcp#206

This problem was asked by Twitter.

A permutation can be specified by an array P, where P[i] represents the location of the element at i in the permutation. For example, [2, 1, 0] represents the permutation where elements at the index 0 and 2 are swapped.

Given an array and a permutation, apply the permutation to the array. For example, given the array ["a", "b", "c"] and the permutation [2, 1, 0], return ["c", "b", "a"].

"""

# Solution #1: use new array. (naive)
# O(n) time
# O(n) space
def apply_perm(arr, perm):
    b = arr[:]

    for i in range(0, len(perm)):
        b[perm[i]] = arr[i]

    return b


# Solution #2: trace out cycles
# O(n) time
# O(1) space - since inner loop not entered for elements already at correct position
# Con: also sorts the permutation
# Can cheat by changing sign of permutation values, but makes this technically O(n),
# even if sign bit unlikely to be used in practice.
def apply_perm2(arr, perm):

    for i in range(0, len(arr)):


        while (perm[i] != i):
            old_target_perm = perm[perm[i]]
            old_target_arr = arr[perm[i]] 
            
            perm[perm[i]] = perm[i]
            arr[perm[i]] = arr[i]

            perm[i] = old_target_perm
            arr[i] = old_target_arr

    return arr


# Solution #3: sort array using permutation values as keys
# Can use custom sort, eg heapsort.
# Instead of writing custom sort, combine elements of array and permutation
# into tuples of new array.
# O(n log n) time
# Another con: permutation is not preserved
def apply_perm3(arr, perm):
    pass # not implemented



"""

0 -> 2
1 -> 1
2 -> 0

"""



arr = ["a", "b", "c"]
perm = [2, 1, 0]

arr = ['a', 'b', 'c', 'd', 'e']
#perm = [0, 1, 2, 3, 4]
perm = [3, 0, 4, 1, 2]

print("\narray = {}".format(arr))
print("permutation = {}\n".format(perm))

new_arr = apply_perm(arr[:], perm[:])
print("new array = {}".format(new_arr))

new_arr2 = apply_perm2(arr[:], perm[:])
print("new array2 = {}".format(new_arr2))


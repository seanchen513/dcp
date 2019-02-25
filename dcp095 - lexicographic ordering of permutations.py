"""
dcp#95

This problem was asked by Palantir.

Given a number represented by a list of digits, find the next greater permutation of a number, in terms of lexicographic ordering. If there is not greater permutation possible, return the permutation with the lowest value/ordering.

For example, the list [1,2,3] should return [1,3,2]. The list [1,3,2] should return [2,1,3]. The list [3,2,1] should return [1,2,3].

Can you perform the operation without allocating extra memory (disregarding the input memory)?
"""


# assume len(a) >= 2
def next(a):

    ### find index of rightmost integer that is smaller than the "next" integer (the one immediately to the right)
    k = len(a) - 2
    while a[k] > a[k+1]:
        k -= 1
        if k == -1:
            return a[::-1]

    ### find smallest integer to right of a[k] that is bigger than a[k]
    ak = a[k]
    #print("ak = {}".format(ak))
    m = len(a) + 1

    for j in range(k + 1, len(a)):
        if a[j] > ak:
            m = min(m, a[j])
            index_m = j

    #print("m = {}".format(m))
    #print("index_m = {}".format(index_m))

    ### swap
    a[k] = a[index_m] 
    a[index_m] = ak
    #print("after swap, list = {}\n".format(a))

    ### reverse list to right of index k to sort it
    return a[:k+1] + a[-1:k:-1]


#a = [1, 2]
#a = [1, 2, 3]
a = [1, 2, 3, 4]

a_orig = a[:]
print("1: {}".format(a))

# import math
# n = math.factorial(len(a))
# for _ in range(n):
#     a = next(a)
#     print(a)

k = 1
while True:
    a = next(a)
    k += 1
    print("{}: {}".format(k, a))
    if a == a_orig:
        break


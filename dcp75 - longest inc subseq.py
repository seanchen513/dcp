'''
dcp#75

This problem was asked by Microsoft.

Given an array of numbers, find the length of the longest increasing subsequence in the array. 
The subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], 
the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
'''



def f2(a, subseq):
    last_val = subseq[-1]

    for i in range(0, len(a)):
        if a[i] > last_val:
            subseq.append(a[i])
            subseq.append(f2(a[i+1:], subseq))

    return subseq


def f1(a, subseq = []):
    if subseq is []:
        for i in range(0, len(a)):
            subseq.append(a[0])
            return f(a[1:], subseq)

    else:
    
        for i in range(0, len(a)):
            if (a[i] > subseq[-1]):
                subseq = f(a[i+1:], a[i])
                length = len(subseq)
                if length > max_len:
                    max_len = length
                    max_subseq = subseq

        return 

'''
Longest increasing subsequence (LIS)

Optimal substructure property:

Given array a, indexed 0..n-1

Let L(i) = length of LIS ending at index i, where 0 <= i <= n-1
Let S(i) = LIS ending at index i

L(i) = 1 + max{L(j): 0 <= j < i and a(j) < a(i)}

S(i) = concatenated sequence [ S(j), a[i] ] where S(j)...

Length of LIS for a = max{L(i) : 0 <= 1 <= n-1 }

'''


def g(a, n, subseq, max_length):
    if n == 1:
        return 1
    
    max_ending_here = 0

    for i in range(0, n-1):
        res = g(a, i, subseq, max_length)

        if (a[i] < a[n-1]) and (res + 1 > max_ending_here):
            max_ending_here = res + 1

    if max_length < max_ending_here:
        max_length = max_ending_here

    return max_ending_here


# Returns an increasing subsequence of "a" of maximum length.
# Uses dynamic programming using tabulation (bottoms-up).
# O(n^2)
def construct_LIS_table(a):
    n = len(a)
    L = [[] for x in range(n)]
    L[0] = [a[0]]

    for i in range(1, n):
        # define L[i] = sequence concatenation of max{ L(j): j < i } and a[i]
        for j in range(0, i):
            if ( a[j] < a[i] ) and ( len(L[j]) > len(L[i]) ):
                L[i] = L[j].copy() # !!!

        L[i].append(a[i])

    # L[i] now stores increasing subsequence of "a" that ends with a[i]
    return L

def get_LIS(table):
    max = table[0] # to hold subsequence of max length
    for x in table:
        if len(x) > len(max):
            max = x

    return max



a = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
# Note: original problem statement gave solution: 0, 2, 6, 9, 11, 15
# Another solution is: 0, 4, 6, 9, 13, 15

# n = len(a)
# subseq = []
# max_length = 0
# seq = g(a, n-1, subseq, max_length)

table = construct_LIS_table(a)
subseq = get_LIS(table)
max_length = len(subseq)

print("original array: {}".format(a))

print("\nLIS table:")
for i, x in enumerate(table):
    print("{}: {}".format(i, x))

print("\nan inc subseq of max length: {}".format(subseq))
print("max_length: {}".format(max_length))
#print("length: {}".format(len(seq)))


'''
dcp#75

This problem was asked by Microsoft.

Given an array of numbers, find the length of the longest increasing subsequence in the array. 
The subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], 
the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
'''

# I give up on naive, recursive solution.

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

# Returns an increasing subsequence of "a" of maximum length.
# Uses dynamic programming using tabulation (bottom-up).
# Creates table L where L[i] = a max-legnth increasing subsequence of "a" that ends with a[i]
# O(n^2)
# Note: there may be more than one max-length inc subsequence of "a" that ends with a[i]
# but the table only stores one of them.
def construct_LIS_table(a):
    n = len(a)
    L = [[] for x in range(n)]
    L[0] = [a[0]]

    for i in range(1, n):
        # define L[i] = sequence concatenation of max{ L(j): j < i } and a[i]
        for j in range(0, i):
            if ( a[j] < a[i] ) and ( len(L[j]) > len(L[i]) ):
                # L[i] = L[j].copy() # Python 3.3+
                # L[i] = list( L[j] )
                L[i] = L[j][:]

        L[i].append(a[i])

    # L[i] now stores increasing subsequence of "a" that ends with a[i]
    return L

# Given table as constructed by construct_LIS_table(), returns list of subsequences of max length
# that are contained in the table.  Note that construct_LIS_table() doesn't return
# all sequences of max length for each given index.
def get_LIS(table):
    max_length = len(table[0])
    maxes = [table[0]] # to hold subsequences of max length
    
    for x in table:
        if len(x) > max_length:
            maxes = [x]
            max_length = len(x)
        elif len(x) == max_length:
            maxes.append(x)

    return maxes



a = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
# Note: original problem statement gave solution: 0, 2, 6, 9, 11, 15
# Another solution is: 0, 4, 6, 9, 13, 15

# n = len(a)
# subseq = []
# max_length = 0
# seq = g(a, n-1, subseq, max_length)

table = construct_LIS_table(a)
subseqs = get_LIS(table)
max_length = len(subseqs[0])

print("original array: {}".format(a))

print("\nLIS table:")
for i, x in enumerate(table):
    print("{}: {}".format(i, x))

print("\nmax_length: {}".format(max_length))
print("\ninc subsequences of max length:")
print(subseqs)




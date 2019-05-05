"""
dcp#214

This problem was asked by Stripe.

Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.

For example, given 156, you should return 3.
"""


def len_max_consecutive_1s(n):
    #b = bin(n) # string with prefix "0b"; also works in this case
    b = '{:b}'.format(n)
    print("binary rep = {}".format(b))
 
    max_len = 0
    length = 0

    for i in range(0, len(b)):
        if b[i] == '1':
            length += 1
        else:
            max_len = max(max_len, length)
            length = 0

    # need to calculate max one more time in case last-read binary digit was 1
    return max(max_len, length)



n = 156 # 3
#n = 1 # 1
#n = 0 # 0
#n = 1024 # 1

l = len_max_consecutive_1s(n)

print("n = {}".format(n))
print("length of longest consecutive run of 1s in binary rep = {}".format(l))


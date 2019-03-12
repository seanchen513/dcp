"""
dcp#156

This problem was asked by Facebook.

Given a positive integer n, find the smallest number of squared integers which sum to n.

For example, given n = 13, return 2 since 13 = 32 + 22 = 9 + 4.

Given n = 27, return 3 since 27 = 32 + 32 + 32 = 9 + 9 + 9.
"""

# squares: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, ...
# Note: n = 1^2 + ... 1^2 is always a solution, so smallest
# number of squared integers which sum to n is at most n.


# Assume n is positive integer.
# Note: using n_sqrt ends up giving wrong answers.
def find_smallest_num_squares(n):
    if n < 4:
        return n

    n_sqrt = n**0.5
    if n_sqrt.is_integer():
        return 1

    num_sq = n # start with case: n = 1^2 + .. + 1^2 (n times)

    for i in range(1, int(n_sqrt) + 1):
    #for i in range(1, n + 1):
    #    if i*i > n:
    #        break

        num_sq = min(num_sq, 1 + find_smallest_num_squares(n - i**2))

    return num_sq


def test(n):
    s = find_smallest_num_squares(n)
    print("\nn = {}".format(n))
    print("smallest num squares that sum to n = {}".format(s))


test(1) # 1
test(2) # 1 + 1
test(3) # 1 + 1 + 1
test(13) # 9 + 4
test(16) # 16
test(27) # 9 + 9 + 9
test(43) # 25 + 18


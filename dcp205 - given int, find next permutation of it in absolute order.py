"""
This problem was asked by IBM.

Given an integer, find the next permutation of it in absolute order. For example, given 48975, the next permutation would be 49578.

"""

# brute force: find all permutations, sort them, find the given permutation, return the next greater one

"""
Solution:
case 1: if all digits sorted desc, then no solution (return None)
case 2: if all digits sorted asc, then swap last 2 digits

other cases:
1. Traversing from right side, find digit d that is smaller than previous digit
2. Of traversed digits, find smallest digit > d.
    - Can use binary search here.
3. Swap these two digits.
4. Sort all digits to right of d (current position).
    - Actually, we know that all these digits are sorted in descending order 
      except for possibly the digit that was swapped in.
    - So this step could be done in O(n) time.

O(n) time
O(n) space since we convert integer to list of digit strings
"""

# Given "num" is integer.
def next_perm(num):
    a = list(map(int, str(num))) # list of digits of num
    n = len(a)
    
    pos1 = None

    for k in range(n-2, -1, -1):
        if a[k] < a[k + 1]:
            pos1 = k
            break

    if pos1 is None: # digits of given integer is descending (left to right), so no solution
        return None

    # k is now position of digit 1
    # Now, of traversed digits, find smallest digit > a[pos1]

    min = 10
    min_index = -1
    for k in range(pos1 + 1, n):
        if ( int(a[k]) > int(a[pos1]) ) and ( int(a[k]) < min ):
            min = a[k]
            min_index = k
    
    # swap these two digits
    a[pos1], a[min_index] = a[min_index], a[pos1]

    # Sort all digits to right of pos1.
    # Actually, we know that all these digits are sorted in descending order 
    # except for possibly the digit that was swapped in.
    # So this step could be done in O(n) time.
    a[pos1 + 1:] = sorted(a[pos1 + 1:])

    # map(str, a) = list of digits, where each digit is a string
    # ''.join() = concatenate the digit-strings into a single string
    # convert string into int
    return int( ''.join( map(str, a) ) )


################################################################################

n = 5 # trivial case; answer = None
n = 12345 # one of the simple cases; answer = 12354 
n = 54321 # one of the simple cases; answer = None
n = 48975 # 49578

next = next_perm(n)

print("n = {}".format(n))
print("next perm = {}".format(next))

###

print("\nIterate through next permutations until None:")

while n is not None:
    print(n)
    n = next_perm(n)


"""
dcp268 medium

This problem was asked by Indeed.

Given a 32-bit positive integer N, determine whether it is a power of four in faster than O(log N) time.
"""

"""
LC342. Power of Four
Easy

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false

Follow up: Could you solve it without loops/recursion?
"""

import math

# math: use log
def power_of_four(n: int) -> bool:
    if n <= 0:
        return False
    
    epsilon = 1e-10
    x = math.log(n, 4)
    
    if abs(x - round(x)) < epsilon:
        return True

    return False

# iteration
def power_of_four2(n: int) -> bool:
    if n <= 0:
        return False
    
    while n > 1:
        n /= 4
        
    return n == 1

# recursion
def power_of_four3(n: int) -> bool:
    if n <= 0:
        return False
    
    if n == 1:
        return True
    
    return power_of_four3(n/4)

# bits: check if only one bit is set (ie, n is power of 2),
# and the only set bit is in an even position (0-based)
def power_of_four4(n: int) -> bool:
    if n <= 0:
        return False
    
    # check if n is power of 2
    if n & (n - 1) != 0:
        return False
    
    # find bit position (0-based)
    bit_pos = -1
    while n:
        bit_pos += 1
        n >>= 1

    return bit_pos % 2 == 0

"""
Solution: bits

Claim: checking (num - 1) % == 0 suffices to distinguish powers of 4
from powers of 2 that are not powers of 4.  That is,
(4^n - 1) % 3 == 0
(2^n - 1) % 3 != 0 when n is odd

Proof:
2^n = (3 - 1)^n = C(n,0) 3^n (-1)^0 + C(n-1, 1) 3^(n-1) (-1)^1 + ... + (-1)^n

All terms have a factor of 3 except the last term, which is 1 or -1.

If n is even, then the last term (-1)^n = 1.  So (2^n - 1) % 3 == 0.
Ie, (4^(n/2) - 1) % 3 == 0.

If n is odd, then the last term (-1)^n = -1.  So (2^n - 1) % 3 == 1 != 0.
"""
def power_of_four5(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0 and (n - 1) % 3 == 0

def power_of_four6(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0 and \
        n & 0b0101_0101_0101_0101_0101_0101_0101_0101 == n

###############################################################################

if __name__ == "__main__":
    nums = [-1, 0, 1, 2, 3, 4, 8, 16, 32, 64, 128, 2**29, 2**30]

    for n in nums:
        print(f"\nn = {n}")
        print(f"sol #1: {power_of_four(n)}")
        print(f"sol #2: {power_of_four2(n)}")
        print(f"sol #3: {power_of_four3(n)}")
        print(f"sol #4: {power_of_four4(n)}")
        print(f"sol #5: {power_of_four5(n)}")
        print(f"sol #6: {power_of_four6(n)}")

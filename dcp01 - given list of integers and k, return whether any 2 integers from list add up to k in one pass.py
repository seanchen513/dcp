"""
dcp#1

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

### Assume distinct integers chosen from list.
### Assume list contains only integers and at least 2 integers.

################################################################################
# Solution #1
# O(n^2), no sorting.
def naive_sums_to(a, target_sum):
    n = len(a)

    for i in range(0, n):
        for j in range(i + 1, n):
            if a[i] + a[j] == target_sum:
                return a[i]
    
    return None

################################################################################
# Solution #2:
# Relies on sorting.  
# One pass.
# Only finds at most one pair of integers in "a" that add up to "sum".
def sums_to(a, target_sum):
    a.sort()

    left = 0
    right = len(a) - 1

    while left < right:
        sum = a[left] + a[right]

        if sum < target_sum:
            left += 1
        elif sum > target_sum:
            right -= 1
        else:
            return a[left]

    return None

################################################################################
# Solution #3:
# Doesn't rely on sorting, but uses set.
#
# O(n) since one pass and set (hashmap) operations (here, lookup and insert)
# are O(1) amortized on average.
# Note: hashmap operations are O(n) worst case if hash buckets are linear,
# or O(log n) if hash buckets are self-balancing binary search trees.
def sums_to2(a, target_sum):
    s = set()

    for k in a:
        if target_sum - k in s:
            return k
        else:
            s.add(k)

    return None

################################################################################

a = [10, 15, 3, 7]
target_sum = 17

#s = naive_sums_to(a, target_sum)
#s = sums_to(a, target_sum)
s = sums_to2(a, target_sum)

print("list = {}".format(a))
print("target sum = {}".format(target_sum))

if s is None:
    print("No 2 integers found in list that add up given sum.")
else:
    print("integers found = {}, {}".format(s, target_sum - s))


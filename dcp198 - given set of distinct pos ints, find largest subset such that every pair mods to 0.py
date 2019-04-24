"""
This problem was asked by Google.

Given a set of distinct positive integers, find the largest subset such that every pair of elements in the subset (i, j) satisfies either i % j = 0 or j % i = 0.

For example, given the set [3, 5, 10, 20, 21], you should return [5, 10, 20]. Given [1, 3, 6, 24], return [1, 3, 6, 24].
"""

# Largest divisible pairs subset.
# Assume non-empty set s of distinct positive integers is given.
# Sort the array, so we only need to check one mod operation per comparison.
# Set integer negative to indicate it's been visited (divisible by another, smaller number in the array).
# This way, it won't be used to form another chain.
def find_max_subset(s):
    s.sort()
    chains = {}
    
    for i in range(0, len(s)):
        if s[i] < 0:
            continue
        
        chains[s[i]] = [s[i]]

        for j in range(i+1, len(s)):
            if s[j] % s[i] == 0:
                chains[s[i]].append(s[j])
                s[j] = -s[j]

    print("\nChains: {}".format(chains))

    _, max_list = max(chains.items(), key=lambda kv: len(kv[1]))
    #max_list = max(chains.values(), key=lambda v: len(v)) # also works

    return max_list


s = [5]
s = [3, 5, 10, 20, 21] # return [5, 10, 20]
#s = [1, 3, 6, 24] # return [1, 3, 6, 24]


print("\nSet = {}".format(s))

max_subset = find_max_subset(s)

print("\nMax subset = {}".format(max_subset))


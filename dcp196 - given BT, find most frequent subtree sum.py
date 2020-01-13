"""
dcp#196

This problem was asked by Apple.

Given the root of a binary tree, find the most frequent subtree sum. The subtree sum of a node is the sum of all values under a node, including the node itself.

For example, given the following tree:

  5
 / \
2  -5
Return 2 as it occurs twice: once as the left leaf, and once as the sum of 2 + 5 - 5.

"""

# Note: in case of ties, report any.

class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_most_frequent_sum_util(root, freqs):
    if root is None:
        return 0

    sum = (root.val + find_most_frequent_sum_util(root.left, freqs) 
        + find_most_frequent_sum_util(root.right, freqs))

    if sum in freqs:
        freqs[sum] += 1
    else:
        freqs[sum] = 1

    return sum


def find_most_frequent_sum(root):
    freqs = {}
     
    find_most_frequent_sum_util(root, freqs)

    sorted_freqs = sorted(freqs.items(), reverse=True)
    
    print("List of (sum, freq) tuples:")
    print(sorted_freqs)
    
    return sorted_freqs[0] # tuple (sum, freq)


root = Node(13)
root = Node(5, Node(2), Node(-5))

n, freq = find_most_frequent_sum(root)

print("\nMost frequent sum is {} with frequency {}".format(n, freq))


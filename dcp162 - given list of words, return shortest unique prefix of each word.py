"""
dcp#162

This problem was asked by Square.

Given a list of words, return the shortest unique prefix of each word. For example, given the list:

    dog
    cat
    apple
    apricot
    fish

Return the list:

    d
    c
    app
    apr
    f

"""

# Clarify that we must assume no word in the list is a prefix of another word in the list.


################################################################################
### Solution #1: naive

# helper method for shortest_unique_prefixes()
def prefix_found_in_another_word(prefix, word, words):
    for word2 in words:
        if word == word2:
            continue
        
        # if prefix in word2: # wrong
        if word2.startswith(prefix):
            return True

    return False

def shortest_unique_prefixes(words):
    prefixes = []

    for word in words:
        prefix = ""
        for letter in word:
            prefix += letter

            if not prefix_found_in_another_word(prefix, word, words):
                prefixes.append(prefix)
                break

    return prefixes

################################################################################
### Solution #2: trie
# https://www.geeksforgeeks.org/find-all-shortest-unique-prefixes-to-represent-each-word-in-a-given-list/

class TrieNode():
    # def __init__(self, val=None, freq=0):
    def __init__(self, freq=0):
        #self.val = val
        self.freq = freq
        self.children = {}


# insert a new string into trie 
def insert(root, string):
    for ch in string:
        if ch in root.children:
            root.children[ch].freq += 1
        else:
            root.children[ch] = TrieNode(freq=1)

        root = root.children[ch]


def find_prefixes_util(root, prefix, prefixes): 
    if root is None:
        return

    # base case 
    if root.freq == 1:
       prefixes.append(prefix)
       prefix = ""
       return
  
    for ch, child in root.children.items():
        prefix += ch
        find_prefixes_util(child, prefix, prefixes)
        prefix = prefix[:-1] # remove character that was added at start of loop


def find_prefixes(words): 
    # construct a trie of all words 
    root = TrieNode()

    for word in words: 
        insert(root, word) 
  
    # Find all prefixes using trie traversal
    # If we use a list, entries aren't usually ordered the way we want.
    prefixes = []
    prefix = ""
    find_prefixes_util(root, prefix, prefixes)

    return prefixes


################################################################################

words = ['dog', 'cat', 'apple', 'apricot', 'fish']
print("\nwords: {}".format(words))

### Solution #1
prefixes = shortest_unique_prefixes(words)
print("\nprefixes: {}".format(prefixes))

### Solution #2
prefixes2 = find_prefixes(words)
print("\nprefixes2: {}".format(prefixes2)) # not ordered

words.sort()
prefixes2.sort()
print("\nwords sorted: {}".format(words))
print("prefixes sorted: {}".format(prefixes2))

# https://www.geeksforgeeks.org/sort-words-lexicographical-order-python/


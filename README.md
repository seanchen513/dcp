# dcp
Daily Coding Problems

Problems from:
https://www.dailycodingproblem.com/

Solutions by me with some help (when needed) from various web sources.

- Not all problems are listed here yet.
- Not all problems listed here have been solved yet.
- The same problem may appear in multiple categories.


## ...


### Bit manipulation
- 6 - implement XOR linked list
- 37 - return power set of set
- 40 - print non-duplicated integer in array
- 60 - can given multiset of integers be partitioned into 2 subsets with same sum
- 85 - given three 32-bit integers x, y, b, return x if b is 1 and y if b is 0, using only math or bit operations
- 88 - implement division of 2 pos integers without using div, mult, or modulus operators
- 109 - given unsigned 8-bit int, swap its even and odd bits
- 137 - implement a bit array
- 148 - given number of bits n, generate a possible gray code for it
- 161 - given 32-bit integer, return the number with its bits reversed
- 221 - return nth sevenish number
- 249 - given array of ints, find max XOR of any 2 
- 268 - given 32-bit pos int N, find whether power of 4 faster than O(log n)
- 310 - find total num of set bits in all ints bw 1 and N
- 317 - write fn to return bitwise AND of all ints bw M and N
- 331 - given string of x and y, how many flips needed so all x's come before all y's
- 332 - given ints M and N, how many pos int pairs (a,b) st a+b=M, a XOR b = N
- 338 - given int N, find next biggest int with same num 1-bits
- 385 - given hex-encoded str that has been XOR'd against a single char, decrypt

### Sets, subsets, ...
- 37 - return power set of set
- 42 - given list of ints and target number k, return subset that adds up to k
- 60 - can given multiset of integers be partitioned into 2 subsets with same sum
- 198 - given set of distinct pos ints, find largest subset such that every pair (i,j) of elements in subset satifies i%j=0 or j%i=0

### Recursion (no trees)
- 173 - flatten a nested dictionary and namespace keys with periods

### Dynamic Programming
- 12 - given staircase with N steps, find number of ways to climb staircase [math]
- 49 - find max sum of any contiguous subarray in O(n) time
- 75 - longest increasing subsequence
- 283 - given int N, return first N regular numbers (evenly divide some power of 60)

### Dynamic Programming - maximum profit from buying and selling stock
- 47 - given stock price array, find max profit from buying then selling
- 193 - given stock price array, find max profit after fees from unlimited buys and sells
- 408 - given stock price array and int k, find max profit from k buys and sells
- 408b - given stock price array and int k, find max profit from unlimited buys and sells

### Ordering and Permutations
- 95 - given num rep by list of digits, find next greater permutation of number in lexicographic ordering
- 96 - given num as list of digits, return all possible permutations
- 157 - given string, determine whether any permutation of it is a palindrome
- 205 - given integer, find next permutation of it in absolute order
- 206, 401 - given array and permutation specified by another array, apply permutation to array
- 228 - given list of numbers, arrange them in order to form largest possible integer

### Lexicographical ordering
- 95 - given num rep by list of digits, find next greater permutation of number in lexicographic ordering
- 205 - given integer, find next permutation of it in absolute order
- 347 - given str of len N and k (can move one of first k letters to end), find lexico smallest string after unlimited num moves

### Searching
- 374 - given sorted arr of distinct ints, return lowest fixed point

### Sorting
- 169 - given LL, sort it in O(n log n) time and constant space
- 228 - given list of numbers, arrange them in order to form largest possible integer
- 271 - given sorted list of ints of len N, find if x is in list wo mult, div, or bit-shift ops in O(log N)
- 306 - given list of N nums, each num at most k places from sorted pos, sort list in O(N log k)
- 386 - given str, sort it in dec order based on freq of chars


## Arrays, Intervals, ...

### Arrays - general and not classified yet
- 189 - given array, return length of longest subarray where all its elements are distinct
- 192 - given array of nonneg ints, can advance at most num steps of current value; return whether you can get to end of array
- 224 - given sorted array, find smallest positive int that is not the sum of a subset of the array, in O(n) time

### Intervals
- 21, 404 - given array of time intervals for classes, find min rooms required
- 77 - return list of intervals where all overlapping intervals have been merged
- 119 - given set of closed intervals, find smallest set of numbers that covers all intervals (same as dcp200)
- 191 - find min num intervals to remove to make rest of intervals non-overlapping
- 200 - given set of intervals, compute smallest set of points that cover it (same as dcp119)
- 397 - given list of jobs with start and end times, find largest subset of compatible jobs

### Rotated arrays/lists
- 58 - find element in rotated sorted array
- 126 - write fn that rotates list by k elts; try without creating copy of list; how many swaps or moves?
- 177 - given LL and pos int k, rotate list to right by k places
- 197 - given array and num k smaller than length of array, rotate array to right k elements in-place
- 203 - given array sorted and rotated with no duplicates, find min element in O(log N) time


## Matrices, Mazes, ...

### Matrices
- 19 - given cost matrix for building row of N houses and K colors, return min cost with no neighboring houses of same color
- 63 - given matrix of chars and target word, return whether word can be found in matrix left-to-right or up-to-down
- 65 - print matrix in spiral
- 76 - given matrix of lowercase letters, find min num columns that can be removed to ensure each row is ordered from top to bottom
- 84 - given matrix of 0s and 1s, return number of islands in matrix
- 136 - given n by m matrix of 0s and 1s, find largest rectangle containing only 1s and return its area
- 151 - given matrix representing image, pixel location, and color C, replace color of given pixel and all adjacent same-colored pixels with C
- 152 - given n numbers and n probs that sum to 1, write fn to generate one of the numbers with its corresponding prob
- 168 - given n by n matrix, rotate it 90 degrees clockwise
- 195 - given n by m matrix with every row and column sorted, and i1, j1, i2, j2, compute num elements smaller than Mi1j1 and larger than Mi2j2
- 302 - given matrix of slashes, backslashes, and spaces, calc num regions
- 315 - given matrix, is it Toeplitz (elts on any given diagonal are same)
- 392 - given matrix of 1s and 0s with one island of 1s, find perimeter of island

### Mazes (matrix traversal):
- 23 - given boolean matrix maze (True is wall), start, and end, find min steps from start to end
- 62 - given ints n and m, find num ways to move from upper left to lower right corner of n-by-m matrix
- 122 - given matrix of ints, find max sum path from upper left to lower right corner
- 158 - given matrix of 0s and 1s (wall), find num ways to move from upper left to lower right corner


## Strings, anagrams, palindromes, balanced strings

### Strings
- ....

### Strings - anagrams
- 111 - given word w and string s, find all starting indices in s which are anagrams of w
- 359 - given str formed by concat words rep integers and anagramming, return ints in sorted order
- 395 - given arr of str, group anagrams together

### Strings - palindromes
- 34 - given string, find palindrome that can be made by inserting fewest chars
- 46 - find longest palindromic contiguous substring
- 121 - given string, can we delete at most k chars to make a palindrome
- 157 - given string, find if any permutation of it is a palindrome
- 167 - given list of words, find all pairs of unique indices such that concatenation of two words is a palindrome
- 181 - given string, split it into as few strings as possible such that each string is a palindrome
- 396 - given str, return length of longest palindromic subseq in str in O(n^2) time and space

### Other palindromes
- 104 - determine if doubly LL is palindrome (what if singly linked) [LL]
- 202 - check whether an integer is a palindrome without converting to string [math]

### Balanced strings
- 27 - given string of round, curly, and square brackets, return whether balanced
- 86 - given string of parentheses, return min num parentheses to be removed to make string valid
- 142 - given string of parentheses and wildcard *, determine whether balanced
- 199 - given string of parentheses, find a balanced string that can be produced from it using min num insertions and deletions


## Linked lists, queues, Stacks, Heaps, Dictionaries

### Linked lists
- 6 - implement XOR linked list
- 20 - find intersecting node of 2 LL's in O(M+N) time and constant space
- 26, 398 - given LL and int k, remove kth last element in constant space and 1 pass
- 73 - given singly LL, reverse it in-place
- 78 - given k sorted singly LL's, merge them into one sorted singly LL
- 104 - given doubly LL, is it palindrome (what if singly linked)
- 127 - given 2 LL's rep ints, return their sum in same format
- 131 - given LL where each node has random pointer, deep clone the list
- 145 - given LL, swap every 2 nodes
- 169 - given LL, sort it in O(n log n) time and constant space
- 177 - given LL and pos int k, rotate list to right by k places
- 208 - given LL of numbers and pivot k, partition LL so all nodes less than k come before all other nodes
- 256 - given LL, rearrange node values so they appear in alternating low high form
- 305 - given LL, remove all consec nodes that sum to zero
- 337 - given LL, uniformly shuffle nodes; what if prioritize space over time

### Queues
- 53 - implement queue using 2 stacks
- 356 - implement queue using set of fixed-length arrays

### Stacks
- 43 - implement stack with push, pop and max, each in constant time
- 141 - implement 3 stacks using a single list
- 154 - implement a stack using only a max heap
- 163 - given arithmetic expression in RPN, evaluate it
- 180 - given stack of n elements, interleave the first half of the stack with the second half reversed using only a queue

### Heaps
- 154 - implement a stack using only a max heap
- 336 - given N ints, how many ways to create max heap
- 377 - given int arr and window of size k, print out median of each window

### Dictionaries, maps, ...
- 92 - given hashmap of key to values (both courseIds) that are prereqs, return sorted ordering of courses such that we can finish all courses
- 97 - write map impl with get function that lets you retrieve value of key at particular time
- 173 - flatten a nested dictionary and namespace keys with periods


## Trees

### Binary trees (BT)
- 3 - serialize deserialize BT
- 8 - given BT, count unival subtrees
- 24 - implement locking in BT
- 50 - evaluate arithmetic expression given by BT
- 80 - given BT, return deepest node
- 83 - invert a BT (sideways)
- 112 - given BT, find lowest common ancestor of two given nodes, where each node has a parent pointer
- 115 - given 2 non-empty BTs s and t, check whether t has exactly same structure and node values with subtree of s
- 116 - generate a finite but arb large BT quickly in O(1)
- 146 - given BT where all nodes are 0 or 1, prune the tree so that all subtrees containing all 0s are removed
- 196 - given BT, find most frequent subtree sum
- 204 - given complete BT, count number of nodes faster than O(n)
- 215 - given BT, return its bottom view
- 247 - given BT, determine whether or not it is height-balanced
- 254 - given BT, convert it to a full one by removing nodes with only one child
- 284 - given BT and partic node, find all cousins
- 326 - given seq, construct Cartesian tree (heap-ordered and in-order)
- 327 - given two BTs, construct BT of sums
- 357 - given BT in certain nested str rep, find depth of tree

### Binary trees - Traversals
- 48 - reconstruct BT from pre-order and in-order traversals
- 107 - print nodes in a BT level-wise
- 117 - given BT, return level of tree with min sum
- 223 - compute in-order traversal of a BT using O(1) space
- 258 - given BT, print nodes in boustrophedon order

### Binary trees (BT) - Paths
- 94 - given BT of ints, find max path sum between 2 nodes
- 110 - given BT, return all paths from root to leaves
- 135 - given BT, find min path sum from root to leaf
- 394 - given BT and int k, return whether there is root-to-leaf path that sums to k

### Binary search trees (BST)
- 36 - given BST, find second largest node
- 89 - given BT, is it BST
- 93, 405 - given tree, find largest subtree that is a BST
- 125 - given BST and target k, return 2 nodes in tree whose sum is k
- 133 - given node in BST, return next bigger element (inorder successor)
- 165 - given array of ints, return new array where each elt is number of smaller ints to right of that elt in original array
- 179 - given sequence of keys visited by postorder traversal of BST, reconstruct tree
- 278 - given int N, construct all poss BST's with N nodes
- 296 - given sorted array, convert to height-balanced BST
- 307 - given BST and int, find floor and ceiling nodes
- 343 - given BST and range [a,b], return sum of elts in BST within range

### Tries
- 11 - implement autocomplete system
- 162 - given list of words, return shortest unique prefix of each word

### Other trees
- 160 - given tree with weighted edges, compute length of longest path
- 237 - given a k-ary tree, determine whether it's symmetric
- 261 - given dict of char freqs, build a Huffman tree, and use it to determine a mapping bw chars and their encoded binary strings
- 344 - given tree with even num nodes, return max num edges that can be removed so subtrees have even num nodes
- 348 - implement insertion and search for ternary search tree


## Graphs

### Graphs - general or not classified yet
- 56 - can given graph be colored using at most k colors
- 72 - given graph represented by string and edge list, return largest value path
- 182 - given an undirected graph, check if it is minimally connected
- 207 - given undirected graph G, check whether it is bipartite
- 218 - write algo to compute reversal of directed graph
- 234 - given undirected graph with weighted edges, compute the maximum weight spanning tree
- 255 - given a graph, find its transitive closure
- 262 - find all bridges in connected undirected graph
- 279 - given friendship adjacency list, find num friend groups
- 280 - given undirected graph, find if it contains a cycle
- 292 - given adjacency list of students and their enemies, find pair of teams if exist
- 294 - given dict of location-elevation and dict mapping paths bw these locs and distances, find len of shortest cycle through 0
- 335 - given directed graph of links bw websites, calc each site's page rank
- 346 - given list of airline ticket prices for direct flights bw cities, find cheapest path from A to B with up to k connections
- 407 - given undirected graph of pipes, find lowest cost config of pipes st each house has access to water


## Math

### Math - general or not classified yet
- 69 - largest product of 3 integers
- 70 - given pos integer n, return nth perfect number (digits sum to 10)
- 74 - num times x appears in n-by-n mult table
- 100 - given infinite 2D grid and seq of points to cover in order, find min num steps
- 129 - given real number n, find square root of n
- 138 - find min number of coins to make n cents
- 156, 350 - given pos int n, find smallest number of squared ints which sum to n
- 198 - given set of distinct pos ints, find largest subset such that every pair (i,j) of elements in subset satifies i%j=0 or j%i=0
- 202 - check whether an integer is a palindrome without converting to string
- 210 - test conjecture that every Collatz sequence eventually reaches one
- 244 - implement Sieve of Eratosthenes
- 252 - create algo to turn a proper fraction into an Egyption fraction
- 283 - given int N, return first N regular nums (evenly divide some power of 60)
- 288 - given n, find num steps to reach Kaprekar's constant from n
- 303 - given clock time hhmm, find angle bw hour and minute hands; when is angle zero
- 372 - write fn that takes natural num and returns num digits it has (no loops)
- 380 - impl int division without using division operator in O(log n)

### Math - Formulas
- 12 - given staircase with N steps, find number of ways to climb staircase [DP]
- 233 - implement fib(n), which returns the nth number in the Fibonacci sequence, using only O(1) space

### Math - Distance
- 150 - given list of points, central point, and int k, find nearest k points from central point
- 340 - given set of pts in plane, find two closest pts
- 376 - find closest coin in Manhattan distance

### Math - Number theory
- 101 - given even number greater than 2, return 2 primes that sum to given number (Goldbach's conjecture)
- 184 - given n numbers, find their gcd

### Math - Probability and random numbers
- 14 - estimate pi to 3 decimal places using Monte Carlo method
- 15 - given stream of elts too large to store in memory, pick random elt from stream with uniform prob
- 45 - implement rand7() from rand5()
- 51 - shuffle card deck given rng 1 to k
- 66 - given toss_biased() that returns 0 or 1, write function to simulate unbiased coin toss
- 71 - implement rand5() given rand7()
- 90 - given integer n and list of integers, randomly generate a number from 0 to n-1 that isn't in list (uniform)
- 152 - given n numbers and n probabilities that sum to 1, write function to generate one of the number with its corresponding prob
- 178 - simulate two probability games and calculate their expected values

## ...

### Arithmetic expressions
- 50 - evaluate arithmetic expression given by BT
- 163 - given arithmetic expression in RPN, evaluate it


### Streams
- 15 - given stream of elts too large to store in memory, pick random elt from stream with uniform prob
- 29 - run-length string encoding and decoding
- 33 - print running median of stream of numbers
- 263 - create sentence checker that takes char stream
- 300 - read text file of (voter_id, candidate_id) as stream and return top 3 candidates at any given time, and report fraud

### Lexical closures (Python), anonymous functions, lambdas, function generators:
- 91 - given Python code, how to fix anonymous functions to behave as expected
- 188 - what will this code print out, can we make it print out what we want


## Iterators, classes, implement data structures

### Iterators
- 139 - given an iterator with methods next() and hasNext(), create a wrapper iterator PeekableInterface...
- 166 - implement a 2D iterator class, initialized with array of arrays, with methods next and has_next
- 367 - given two sorted iterators, merge them into one iterator (without pulling in their contents)

### Classes
- 132 - design and implement HitCounter class that keeps track of requests (hits)
- 166 - implement a 2D iterator class, initialized with array of arrays, with methods next and has_next
- 232 - implement a PrefixMapSum class
- 319 - design class to rep 8-puzzle game board, and find steps to solve

### Implement data structure
- 301 - 
- 356 - implement queue using set of fixed-length arrays
- 358 - implement key-value data struct w O(1) ops
- 365 - implement data struct with stack and queue props, using stacks, O(1) extra memory, so amortized times for ops are O(1)
- 368 - implement key value store, where keys and values are ints


## Chess, games, other

### Chess, backtracking
- 38 - N queens problem
- 64 - write function to return number of knight's tours on N-by-N chessboard
- 68 - given list of bishop positions, return num pairs of bishops that can attack each other
- 267 - given chessboard with black king and white pieces, is king in check
- 304 - after k random moves, calc prob knight still remains on chessboard

### Games (not chess)
- 39 - implement Conway's Game of Life
- 54 - implement efficient Sudoku solver
- 128 - write function that prints out all steps to complete Tower of Hanoi
- 219 - design and implement Connect 4
- 225 - given n and k, write algorithm to determine where a prisoner should stand in order to be the last survivor
- 227 - given game board and dict of valid words, implement Boggle solver
- 289 - given starting [a,b,c] for game of Nim and optimal play, find if first player has a forced win

### Other
- 11 - implement autocomplete system
- 55 - implement URL shortener
- 59 - implement file syncing algo over low-bandwidth network
- 120 - implement singleton pattern variation with 2 instances where getInstance() returns alternating instances
- 183 - describe what happens when you type a URL into browser and press Enter
- 263 - create sentence checker that takes char stream
- 328 - implement Elo rating system
- 354 - design system to crawl and copy all of Wikipedia using distributed network of machines
- 369 - implement API for tracking stock price
- 387 - explain the diff bw an API and SDK to a non-technical person
- 388 - explain web cookies to someone non-technical
- 389 - explain diff bw composition and inheritance, and in which cases would you use each
		

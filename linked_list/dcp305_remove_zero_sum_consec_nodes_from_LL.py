"""
dcp305, 417
LC1171 (medium)

This problem was asked by Amazon.

Given a linked list, remove all consecutive nodes that sum to zero. Print out the remaining nodes.

For example, suppose you are given the input 3 -> 4 -> -7 -> 5 -> -6 -> 6. In this case, you should first remove 3 -> 4 -> -7, then -6 -> 6, leaving only 5

"""

# Clarify: should removal of nodes be recursive in that the final list
# have no consecutive nodes that sum to zero?  Assume yes.


class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}, {self.next.__repr__()}"


# Build singly linked list using values from given iterator "it".
# Returns both head and tail.
def build_ll(it):
    if it is None:
        return None, None

    # works for dict and set, but it's probably not well-defined behavior
    if type(it) in [range, list]:
        it = iter(it)

    val = next(it, None)
    head = Node(val)
    tail = head
    
    val = next(it, None)
    while val is not None:
        tail.next = Node(val)
        tail = tail.next
        val = next(it, None)

    return head, tail


def ll_equals(l1, l2):
    while l1 and l2:
        if l1.val != l2.val:
            return False
        
        l1 = l1.next
        l2 = l2.next

    if l1 or l2:
        return False

    return True


###############################################################################

"""
Solution#1: without using an array; no recursion.

Don't have to worry about ever decrementing "start" node
because if that was ever necessary (because we want to calculate
sums going further back after having removed some nodes),
it would have been already detected as part of a zero sum of a larger
sequence.

That is, let S1 is a sequence and sum(S1) = 0.
After removing S1, suppose there is a sequence S2 with sum(S2) = 0
and S2 has an element that is adjacent to S1 in the original array, 
ie, S1 and S2 are disjoint and form a contiguous subsequence S.  Then that 
subsequence S also has sum(S) = 0.  If S2 contains an element that
comes before any element in S1, then the algorithm would detect
that sum(S2) = 0 before sum(S1) = 0, and remove S2 first.
"""
def remove_nodes(head):
    ### First, deal with sums starting at head.

    sum = 0
    curr = head
    
    while curr:
        sum += curr.val
        if sum == 0:
            head = curr.next
            sum = 0

        curr = curr.next

    ### Deal with sums starting at nodes other than head.
    # Now, either (1) head is None, or (2) head is not None and there 
    # is no sum starting at head that sums to 0.

    start = head # sums do not include value of start node

    while start and start.next:
        #print("head = {}, start = {}".format(head.val, start.val))
        sum = 0
        curr = start.next

        while curr:
            sum += curr.val
            #print("   curr = {}, sum = {}".format(curr.val, sum))

            if sum == 0:
                start.next = curr.next
                break

            curr = curr.next 
        
        # if start was updated, don't increment it; check it again
        if sum != 0: 
            start = start.next

    return head


###############################################################################
"""
Solution#2: without using an array; recursive
"""
def remove_nodes2(head):
    ### Deal with sums starting at head. (base case)

    sum = 0
    curr = head
    
    while curr:
        sum += curr.val
        if sum == 0:
            head = curr.next
            sum = 0

        curr = curr.next

    ### Deal with sums starting at nodes other than head.

    start = head

    while start:
        start.next = remove_nodes2(start.next)
        start = start.next

    return head


###############################################################################

# For solution#3
def remove_from_arr(arr):
    n = len(arr)

    for start in range(n):
        sum = 0

        for end in range(start, n):
            sum += arr[end]
            
            if sum == 0: # then remove indices from start to end
                del arr[start:end+1]
                return remove_from_arr(arr)

    return arr


"""
Solution#3: Convert to array, solve, convert back to linked list.
"""
def remove_nodes3(head):
    ### 1. Convert linked list to array
    
    curr = head
    arr = []

    while curr:
        arr.append(curr.val)
        curr = curr.next

    #print("# before any removals: ", arr)

    ### 2. Remove consecutive elements of array that sum to 0

    arr = remove_from_arr(arr)
    #print("# final after all removals: ", arr)
 
    ### 3. Convert final array to linked list and return

    if arr == []:
        return None
    
    n = len(arr)
    new_head = Node(arr[0])
    tail = new_head

    for i in range(1, n):
        tail.next = Node(arr[i])
        tail = tail.next

    return new_head



###############################################################################

import copy

def test(lst, answer={}): # default answer is sentinel for no answer given
    print()

    head1, _ = build_ll(lst)
    head2 = copy.deepcopy(head1)
    head3 = copy.deepcopy(head1)

    #print("\nOriginal linked list:")
    print(head1)
    
    head1 = remove_nodes(head1)
    head2 = remove_nodes2(head2)
    head3 = remove_nodes3(head3)
    
    #print("\nAfter removing consecutive nodes that sum to 0:")
    print("sol#1: ", head1)
    print("sol#2: ", head2)
    print("sol#3: ", head3)

    if answer != {}:
        head_answer, _ = build_ll(answer)
        assert(ll_equals(head1, head_answer))
        assert(ll_equals(head2, head_answer))
        assert(ll_equals(head3, head_answer))


def test_lists(lists_answers):
    for lst, answer in lists_answers:
        test(lst, answer)


# Each answer might not a unique answer, but is what my system produces.
lists_answers = [
    (None, 
        None ),
    ([0], 
        None ),
    ([1], 
        [1] ),
    ([-1, 1], 
        None ),

    ([3, 4, -7, 5, -6, 6],  
        [5] ), # dcp305

    ([3, -3, -7, 5, -6, 6], 
        [-7, 5] ), # check start and end of list
    ([3, -3, -7, 7, -6, 5], 
        [-6, 5] ), # separate sequences at start that sum to 0
    ([3, 4, -8, 8, -6, 6], 
        [3, 4] ), # separate sequences at end that sum to 0
    ([0, 0, 3, 4, -8, 0, 0, 8, 0, -6, 6, -4, 0, 0], 
        [3] ),

    ([1, 2, -3, 3, 1], 
        [3, 1] ), # LC1171 example 1
    ([1, 2, 3, -3, 4], 
        [1, 2, 4] ), # LC1171 example 2
    ([1, 2, 3, -3, -2], 
       [1] ), # LC1171 example 3
]

test_lists(lists_answers)

### to test single list:
lst = [3, 4, -7, 5, -6, 6] # dcp305
#test(lst)


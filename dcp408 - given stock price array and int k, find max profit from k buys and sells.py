"""
dcp#408

This problem was asked by Facebook.

Given an array of numbers representing the stock prices of a company in chronological order and an integer k, return the maximum profit you can make from k buys and sells. You must buy the stock before you can sell it, and you must sell the stock before you can buy it again.

For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3.
"""

"""
Solution: dynamic programming, tabulation

Let P[k][i] be max profit using at most k transactions until ith day.
A transaction is a buy/sell pair with the sell on the ith day.

P[# transactions][day #]

P[k][i] = max(
    P[k][i - 1],
    max( prices[i] - prices[j] + P[k-1][j] : j = 0, ..., i - 1 )
)

where:

P[k][i - 1] : no transactions on ith day

prices[i] - prices[j] + P[k-1][j] :
    kth transaction (sell) on ith day, with corresponding buy on jth day

"""
def max_profit(prices, k):
    n = len(prices)
    
    # this is the "P" in the note above
    # profit[num transactions][ith day]
    # row index = num transactions = 0, 1, ..., k
    # col index = day number = 0, 1, ..., n-1
    profit = [[0]*n for _ in range(k+1)]

    # first row of profit () is all 0s since no transactions
    # first column of profit () is all 0s since 0th day

    for n_trans in range(1, k+1):
        for i in range(1, n):
            # max_so_far = 0
            # for j in range(i):
            #     curr_price = prices[i] - prices[j] + profit[n_trans - 1][j]
            #     if max_so_far < curr_price:
            #         max_so_far = curr_price

            # Simplification #1:
            # use list comprehension instead
            #max_so_far = max( prices[i] - prices[j] + profit[n_trans - 1][j] for j in range(i) )

            # Simplification #2:
            # pull out prices[i] from list comprehension since not dep on j
            max_so_far = prices[i] + max( -prices[j] + profit[n_trans - 1][j] for j in range(i) )

            profit[n_trans][i] = max(profit[n_trans][i-1], max_so_far)

    return profit[k][n-1]


###############################################################################

# Optimized further
def max_profit2(prices, k):
    n = len(prices)
    profit = [[0]*n for _ in range(k+1)]

    for n_trans in range(1, k+1):
        prev_diff = -2**31

        for i in range(1, n):

            # before optimization:
            #max_so_far = prices[i] + max( -prices[j] + profit[n_trans - 1][j] for j in range(i) )
            
            prev_diff = max(prev_diff, -prices[i-1] + profit[n_trans - 1][i-1])
            max_so_far = prices[i] + prev_diff

            profit[n_trans][i] = max(profit[n_trans][i-1], max_so_far)

    return profit[k][n-1]


###############################################################################


prices = [5, 2, 4, 0, 1]
k = 2

#m = max_profit(prices, k)
m = max_profit2(prices, k)

print("\nstock prices = {}".format(prices))
print("\nnumber of buys and sells = {}".format(k))
print("\nmax profit (sol#1) = {}".format(m))


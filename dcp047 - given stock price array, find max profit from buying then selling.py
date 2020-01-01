"""
dcp#47

This problem was asked by Facebook.

Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.
"""

# Solution#1: naive
# O(n^2)
def max_profit(prices):
    m = 0 
    n = len(prices)

    for i in range(n):
        buy_price = prices[i]

        for j in range(i+1, n):
            m = max(prices[j] - buy_price, m)

    return m


# Solution#2:
# Iterate through prices, keeping track of min so far
# and current price minus min so far
# O(n)
def max_profit2(prices):
    min_so_far = prices[0]
    p = 0 # max profit so far

    for price in prices:
        min_so_far = min(price, min_so_far)
        p = max(price - min_so_far, p)

    return p


###############################################################################

# For use by max_profits3()
# https://codereview.stackexchange.com/questions/138088/buy-once-and-sell-once-for-maximum-profit

def profits(prices):
    prices = iter(prices)
    least = next(prices)
    
    yield 0

    for price in prices:
        least = min(least, price)
        yield price - least


# Solution#3
# Essentially the same as solution#2 but uses custom generator fn profits().
def max_profit3(prices):
    return max(profits(prices))


###############################################################################

#prices = [1, 2, 3, 4, 5]
#prices = [5, 4, 3, 2, 1]
#prices = [1, 2, 3, 4, 3, 5]
prices = [9, 11, 8, 5, 7, 10] # given by problem

m = max_profit(prices)
m2 = max_profit2(prices)
m3 = max_profit3(prices)

print("\nstock prices = {}".format(prices))
print("\nmax profit from buying then selling (sol#1) = {}".format(m))
print("\nmax profit from buying then selling (sol#2) = {}".format(m2))
print("\nmax profit from buying then selling (sol#3) = {}".format(m3))


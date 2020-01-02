"""
Given stock price array and int k, find max profit from k buys and sells.
*** Must sell all stock before buying again.

Related problems:

dcp47 - given stock price array, find max profit from buying then selling
dcp193 - given stock price array, find max profit after fees from unlimited buys and sells
    (*** don't have to sell before buying again)
dcp408 - given stock price array and int k, find max profit from k buys and sells

"""


"""
Solution: buy at local minima, sell at local maxima
O(n)

We always want to sell at a higher price S than the buy price B.
Suppose the prices in the range (B, S) is non-decreasing.
It wouldn't make sense to buy at a later point in this interval,
or to sell at an earlier point in this interval, or to conduct
multiple transactions within this interval.
We can make the profit even greater if the interval can be extended
while maintaining non-decreasing prices.
The interval can be made maximal by taking B to be a local minimum
for prices, and S to be a local maximum.
"""
def max_profit(prices):
    n = len(prices)
    buy_index = 0
    profit = 0

    for i in range(1, n):
        if prices[i] < prices[i - 1]:
            buy_index = i # update local minimum
            continue

        # if local maximum (might be end of array)
        if (prices[i] > prices[i - 1]) and \
        (i == n - 1 or prices[i] > prices[i + 1]):
            sell_index = i

            p = prices[sell_index] - prices[buy_index]
            profit += p

            print("\nBuying at index {} for price {}".format(buy_index, prices[buy_index]))
            print("Selling at index {} for price {}".format(sell_index, prices[sell_index]))
            print("Profit = {}".format(p))

    return profit


###############################################################################

prices = [5, 2, 4, 0, 1]
prices = [1, 3, 2, 8, 4, 10]

print("\nstock prices = {}".format(prices))
print("#"*80)

m = max_profit(prices)

print("#"*80)
print("\nmax profit = {}".format(m))


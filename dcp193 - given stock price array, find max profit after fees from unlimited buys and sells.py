"""
dcp#193
LC#714

This problem was asked by Affirm.

Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock. You're also given a number fee that represents a transaction fee for each buy and sell transaction.

You must buy before you can sell the stock, but you can make as many transactions as you like.

For example, given [1, 3, 2, 8, 4, 10] and fee = 2, you should return 9, since you could buy the stock at 1 dollar, and sell at 8 dollars, and then buy it at 4 dollars and sell it at 10 dollars. Since we did two transactions, there is a 4 dollar fee, so we have 7 + 6 = 13 profit minus 4 dollars of fees.
"""


"""
Solution: from LC#714
O(n)

Interesting post:
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108870/Most-consistent-ways-of-dealing-with-the-series-of-stock-problems
"""
def max_profit(prices, fee=0):
    n = len(prices)
    cash = 0 # max profit if we don't hold stock at end of current period
    hold = -prices[0] # max profit if we hold stock at end of current period

    print("i = {}\tcash = {}\thold = {}".format(0, cash, hold))
    
    for i in range(1, n):
        # If end this period with all cash and no stock
        # Scenario 1: no stock prior period i-1, and don't buy stock now
        # Scenario 2: had stock prior period, sell it now
        cash = max(cash, hold + prices[i] - fee)
    
        # If end this period holding a stock
        # Scenario 1: had stock prior period i-1, and don't sell now
        # Scenario 2: had no stock prior period, and buy now
        hold = max(hold, cash - prices[i])
        
        print("i = {}\tcash = {}\thold = {}".format(i, cash, hold))

    return cash


###############################################################################

prices = [5, 2, 4, 0, 1]
prices = [1, 3, 2, 8, 4, 10] # for fee = 2, answer = 9
fee = 2

print("\nstock prices = {}".format(prices))
print("\nfee per buy or sell = {}".format(fee))
print("\n" + "#"*80 + "\n")

m = max_profit(prices, fee)

print("\n" + "#"*80)
print("\nmax profit = {}".format(m))


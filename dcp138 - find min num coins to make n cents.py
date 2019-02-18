"""
dcp#138

This problem was asked by Google.

Find the minimum number of coins required to make n cents.

You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.

For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.
"""

def num_coins(n):
    quarters = n // 25
    left = n % 25 

    dimes = left // 10
    left = left % 10

    nickels = left // 5
    
    pennies = left % 5

    return quarters + dimes + nickels + pennies
    

n = 1
n = 0
n = 41
n = 100
n = 164
n = 16
coins = num_coins(n)

print("Total number of coins to make {} cents: {}".format(n, coins))


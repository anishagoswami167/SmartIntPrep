#Best Time to Buy and Sell Stock
prices = [7,1,5,3,6,4,23]
#Output:5

def buyStock(prices):
    minPrice=prices[0]
    profit=0
    
    for p in prices:
        if minPrice>p:
            minPrice=p
        if p-minPrice>profit:
            profit=p-minPrice
            
    return profit
print(buyStock(prices))


def buyStock(prices):
    minPrice = prices[0]
    profit = 0

    for p in prices:

        minPrice = min(minPrice, p)

        profit = max(profit, p - minPrice)

    return profit

# Time: O(n)
# Space: O(1)

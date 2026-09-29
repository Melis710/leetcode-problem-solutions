class Solution:
    # time complexity: O(N)
    # space complexity: O(1)
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]  # initialize buy price (at least one element)
        max_profit = 0  # max_profit can be minimum 0 when buy = sell
        
        for price in prices:  # if price in future less, move buy price to it
            if price <= buy:
                buy = price
            elif price - buy > max_profit:  # when sell price greater we can make profit
                max_profit = price - buy
    
        return max_profit
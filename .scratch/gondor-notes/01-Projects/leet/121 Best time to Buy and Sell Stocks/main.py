# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# To solve this problem, you can use a simple one-pass algorithm. The idea is to keep track of the minimum price encountered so far and calculate the maximum profit by comparing the current price with the minimum price. Here’s a Python function to achieve this:
# This function iterates through the list of prices once, making it efficient with a time complexity of O(n). It keeps updating the minimum price and the maximum profit as it goes through the list. If no profit can be made, it returns 0.
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i, buy in enumerate(prices):
            for _, sell in enumerate(prices[i+1:]):
                if sell - buy > max_profit:
                    max_profit = sell - buy

        return max_profit if max_profit > 0 else 0 

    def maxProfitDp(self, prices: List[int]) -> int:
        # [7,1,5,3,6,4]   
        # mxProfit with 7,  or without 7. 
        # mxProfit of single element = 0
        # mxProfit of two elements = idx2-idx1
       # base case
       if len(prices) < 2:
           return 0
       elif len(prices) == 2:
           pnl =  prices[1] - prices[0] 
           return pnl if pnl > 0 else 0
       else:
           pnl_with_firstel = self.maxProfitDp()
           pnl_without_first_el = self.maxProfitDp(prices[1:])
           return pnl_with_firstel if pnl_with_firstel > pnl_without_first_el else pnl_without_first_el
     


    def maxProfitOnePass(self, prices:List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return int(max_profit)






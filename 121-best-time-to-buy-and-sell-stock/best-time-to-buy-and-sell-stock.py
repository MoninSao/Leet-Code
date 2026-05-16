class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        profit = 0
        profit_list = []
        
        for price in prices:
            if price < lowest:
                lowest = price
            profit = price - lowest
            profit_list.append(profit)

        return max(profit_list)
        
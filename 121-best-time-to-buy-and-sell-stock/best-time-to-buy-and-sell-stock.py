class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_list = []
        profit = 0
        lowest = prices[0]

        for price in prices:
            if price < lowest:
                lowest = price
            profit = price - lowest
            profit_list.append(profit)

        return max(profit_list)
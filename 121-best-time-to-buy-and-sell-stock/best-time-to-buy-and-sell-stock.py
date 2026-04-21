class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        profit = 0
        output = []

        for price in prices:
            if price < lowest:
                lowest = price
            profit = price - lowest
            output.append(profit)

        return max(output)
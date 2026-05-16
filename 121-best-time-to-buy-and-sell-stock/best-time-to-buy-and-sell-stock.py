class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        profit = 0
        output = []
        for i, prc in enumerate(prices):
            if prc < lowest:
                lowest = prc 
            profit = prc - lowest
            output.append(profit)

        return max(output)
            

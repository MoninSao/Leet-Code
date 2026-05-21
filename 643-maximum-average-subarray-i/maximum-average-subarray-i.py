class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curSum = 0 
        maxSum = 0

        for i in range(k):
            curSum += nums[i]

        maxSum = curSum / k

        for i in range(k, len(nums)):
            curSum += nums[i]
            curSum -= nums[i-k]

            avg = curSum / k
            maxSum = max(maxSum, avg)

        return maxSum 
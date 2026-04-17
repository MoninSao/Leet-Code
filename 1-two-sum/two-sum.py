class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in output:
                return [output[complement], i]
            output[num] = i
        
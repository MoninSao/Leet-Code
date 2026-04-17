class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        output = {}
        for i, num in enumerate(nums):
            if num in output:
                return True
            output[num] = i
        return False
        
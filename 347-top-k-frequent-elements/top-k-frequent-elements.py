class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = {}
        
        for num in set(nums):
            counted = nums.count(num)
            if num not in group:
                group[num] = counted 

        sorted_nums = sorted(group, key=lambda x: group[x], reverse = True)

        return sorted_nums[:k]
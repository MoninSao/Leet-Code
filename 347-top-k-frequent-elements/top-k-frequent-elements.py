class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = {}
        for num in set(nums):
            group[num] = nums.count(num)

        sort_group = sorted(group, key = lambda x: group[x] , reverse = True)
        return (sort_group[:k])
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = Counter(nums)

        sort_group = sorted(group, key = lambda x: group[x] , reverse = True)
        return (sort_group[:k])
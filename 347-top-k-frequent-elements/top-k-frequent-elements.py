class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = {}
        
        group = Counter(nums)
           

        sorted_nums = sorted(group, key=lambda x: group[x], reverse = True)


        return sorted_nums[:k]
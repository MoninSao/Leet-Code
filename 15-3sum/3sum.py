class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sorted_nums = sorted(nums)
        output = []

        for i, a in enumerate(sorted_nums):
            # checking for duplicates to skip them since left and right are sorted so we can find them easily next to each other
            if i > 0 and a == sorted_nums[i-1]:
                continue
            
            l = i+1
            r = len(sorted_nums) -1
            while l < r:
                threeSum = a + sorted_nums[l] + sorted_nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1

                else:
                    output.append([a, sorted_nums[r], sorted_nums[l]])
                    l+=1
                    while sorted_nums[l] == sorted_nums[l-1] and l < r:
                        l += 1

        return output


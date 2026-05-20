class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = 0
        l = 0
        charSet = set()

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+= 1
            charSet.add(s[r])
            output = max(output, r - l + 1)

        return output
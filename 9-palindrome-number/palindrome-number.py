class Solution(object):
    def isPalindrome(self, x):
        m = str(x)
        return m == m[::-1]     
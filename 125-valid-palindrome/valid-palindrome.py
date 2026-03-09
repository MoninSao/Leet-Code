class Solution(object):
    def isPalindrome(self, s):
        s = ("".join(c for c in s if c.isalnum())).lower()
        r = s[::-1].lower()
        return r == s
        
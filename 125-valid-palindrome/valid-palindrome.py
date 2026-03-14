class Solution:
    def isPalindrome(self, s: str) -> bool:
        m = ("".join(char for char in s if char.isalnum())).lower()
        s = m[::-1]
        return s == m
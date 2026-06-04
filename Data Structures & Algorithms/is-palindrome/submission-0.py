class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())
        if (s[::-1] == s):
            return True
        else:
            return False
        
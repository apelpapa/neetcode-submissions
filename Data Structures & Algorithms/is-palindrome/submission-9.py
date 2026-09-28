class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"[^A-Za-z0-9]", "", s).lower()
        if s == s[::-1]:
            return True
        return False
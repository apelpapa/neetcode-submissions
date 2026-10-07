class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        left = 0
        res = 0

        for i, ch in enumerate(s):
            while ch in substring:
                substring.remove(s[left])
                left += 1
            substring.add(ch)
            if res < i - left + 1:
                res = i - left + 1
        
        return res
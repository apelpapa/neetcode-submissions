class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s and t:
            s = list(s)
            t = list(t)
            s.sort()
            t.sort()
            if s == t:
                return True
            return False
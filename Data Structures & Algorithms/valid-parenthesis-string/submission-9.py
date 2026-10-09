class Solution:
    def checkValidString(self, s: str) -> bool:
        open_min = 0
        open_max = 0

        for i, ch in enumerate(s):
            if ch == "(":
                open_min += 1
                open_max += 1
            elif ch == ")":
                open_min -= 1
                open_max -= 1
            elif ch == "*":
                open_min -= 1
                open_max += 1
            if open_max < 0:
                return False
            if open_min < 0:
                open_min = 0
        
        return not open_min
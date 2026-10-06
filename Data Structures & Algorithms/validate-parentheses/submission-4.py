class Solution:
    def isValid(self, s: str) -> bool:
        closers = {
            "]": "[",
            ")": "(",
            "}": "{",
        }
        stack = []

        for ch in s:
            if ch in closers:
                if stack and stack[-1] == closers[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        
        return False if stack else True
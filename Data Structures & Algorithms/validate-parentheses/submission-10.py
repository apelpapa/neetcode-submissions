class Solution:
    def isValid(self, s: str) -> bool:
        closers = {"}":"{", "]":"[", ")":"("}
        stack = []
        
        for i, ch in enumerate(s):
            if ch in closers:
                if not stack:
                    return False
                if stack[-1] == closers[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        
        return not stack
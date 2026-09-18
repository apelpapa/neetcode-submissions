class Solution:
    def isValid(self, s: str) -> bool:
        count_old = 0
        count_new = len(s)
        stack = []
        while count_old != count_new and len(s) > 0:
            count_old = count_new

            if len(stack) == 0:
                stack.insert(0, s[0])
                s = s[1:]
            elif s[0] == "(" or s[0] == "[" or s[0] == "{":
                stack.insert(0, s[0])
                s = s[1:]
            elif stack[0] == "(" and s[0] == ")":
                stack.pop(0)
                s = s[1:]
                old_count = 0
            elif stack[0] == "[" and s[0] == "]":
                stack.pop(0)
                s = s[1:]
                old_count = 0
            elif stack[0] == "{" and s[0] == "}":
                stack.pop(0)
                s = s[1:]
                old_count = 0
            count_new = len(s)
        if len(s) == 0 and len(stack) == 0:
            return True
        else:
            return False
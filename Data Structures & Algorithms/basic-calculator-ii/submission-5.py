class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        stack = []
        op = "+"
        num = 0

        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            if not ch.isdigit() or i == len(s) - 1:
                if op == "+":
                    stack.append(num)
                elif op == "-":
                    stack.append(-num)
                elif op == "*":
                    stack.append(num * stack.pop())
                elif op == "/":
                    temp = stack.pop()
                    stack.append(int(temp / num))
                op = ch
                num = 0
        
        return sum(stack)
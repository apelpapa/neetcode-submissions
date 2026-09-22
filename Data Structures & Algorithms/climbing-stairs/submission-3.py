class Solution:
    def climbStairs(self, n: int) -> int:
        step = 0
        new_poss = 0
        poss = 0
        last_poss = 0
        while step <= n:
            print(step, new_poss, poss, last_poss)
            new_poss = poss + last_poss
            if step == n:
                return new_poss
            if step <= 1:
                poss = 1
            last_poss = poss
            poss = new_poss
            step += 1
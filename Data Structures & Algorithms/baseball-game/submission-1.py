class Solution:
    def calPoints(self, operations: List[str]) -> int:
        tracker = []
        for op in operations:
            try: 
                tracker.append(int(op))
            except ValueError:
                if op == "+":
                    tracker.append(tracker[-1] + tracker[-2])
                elif op == "D":
                    tracker.append(tracker[-1]*2)
                elif op == "C":
                    tracker.pop()
        sum_tracker = 0
        for num in tracker:
            sum_tracker += num
        return sum_tracker
        
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []

        for i, inter in enumerate(intervals):
            if len(res) == 0:
                res.append(inter)
            elif res[-1][1] >= inter[0]:
                if res[-1][1] < inter[1]:
                    res[-1][1] = inter[1]
            else:
                res.append(inter)
        return res
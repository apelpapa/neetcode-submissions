class MedianFinder:
    def __init__(self):
        self.lower = []
        self.upper = []

    def addNum(self, num: int) -> None:
        if not self.lower:
            self.lower.append(num)
            return

        if num <= self.lower[-1]:
            self.lower.append(num)
            self.lower[-1], self.lower[-2] = self.lower[-2], self.lower[-1]
        else:
            self.upper.append(num)
            if num < self.upper[0]:
                self.upper[0], self.upper[-1] = self.upper[-1], self.upper[0]

        if len(self.lower) > len(self.upper) + 1:
            self.upper.append(self.lower.pop())
            self.upper[0], self.upper[-1] = self.upper[-1], self.upper[0]
            i = max(range(len(self.lower)), key=self.lower.__getitem__)
            self.lower[i], self.lower[-1] = self.lower[-1], self.lower[i]

        elif len(self.upper) > len(self.lower) + 1:
            self.upper[0], self.upper[-1] = self.upper[-1], self.upper[0]
            self.lower.append(self.upper.pop())
            i = min(range(len(self.upper)), key=self.upper.__getitem__)
            self.upper[i], self.upper[0] = self.upper[0], self.upper[i]

    def findMedian(self) -> float:
        if len(self.lower) > len(self.upper):
            return self.lower[-1]
        if len(self.upper) > len(self.lower):
            return self.upper[0]
        return (self.lower[-1] + self.upper[0]) / 2

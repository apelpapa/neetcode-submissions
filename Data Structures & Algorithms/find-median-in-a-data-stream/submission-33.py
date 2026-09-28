class MedianFinder:
    def __init__(self):
        self.lower = []
        self.upper = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lower, -1 * num)
        if not self.upper and len(self.lower) == 1:
            return None
        if not self.upper:
            heapq.heappush(self.upper, -1 * heapq.heappop(self.lower))

        if len(self.lower) > len(self.upper) + 1:
            heapq.heappush(self.upper, -1 * heapq.heappop(self.lower))

        if (-1 * self.lower[0]) > self.upper[0]:
            heapq.heappush(self.upper, -1 * heapq.heappop(self.lower))
            heapq.heappush(self.lower, -1 * heapq.heappop(self.upper))

    def findMedian(self) -> float:
        if (len(self.lower) + len(self.upper)) % 2 == 1:
            return -1 * self.lower[0]
        else:
            return (-1 * self.lower[0] + self.upper[0]) / 2

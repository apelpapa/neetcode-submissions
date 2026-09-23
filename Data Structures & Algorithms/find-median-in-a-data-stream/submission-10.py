class MedianFinder:

    def __init__(self):
        self.arr = []
        self.length = 0
        

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.length += 1
        self.arr.sort()

    def findMedian(self) -> float:
        median_index = math.floor(self.length / 2)
        if self.length % 2 == 0 and self.length > 1:
            median_arr = [self.arr[median_index - 1], self.arr[median_index]]
            return (median_arr[0] + median_arr[1]) / 2
        else:
            return self.arr[median_index]
        
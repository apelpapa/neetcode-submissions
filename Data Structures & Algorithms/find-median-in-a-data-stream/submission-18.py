class MedianFinder:

    def __init__(self):
        self.lower = []
        self.upper = []

    def addNum(self, num: int) -> None:
        if self.lower == []:
            self.lower.append(num)
            return None
        if self.upper == []:
            self.upper.append(num)
            return None

        if len(self.lower) == 1 and len(self.lower) == len(self.upper):
            if self.lower[0] > self.upper[0]:
                temp = self.lower[0]
                self.lower[0] = self.upper[0]
                self.upper[0] = temp
        

        if num > self.lower[-1] and num < self.upper[0]:
            if len(self.lower) <= len(self.upper):
                self.lower.append(num)
            else:
                self.upper.insert(0, num)
        
        elif num <= self.lower[-1]:
            self.lower.insert(0, num)
        
        else:
            self.upper.append(num)

        if len(self.lower) > len(self.upper) + 1:
            self.upper.insert(0, self.lower.pop())
            temp_max = max(self.lower)
            if temp_max != self.lower[-1]:
                temp_index = self.lower.index(temp_max)
                self.lower[temp_index] = self.lower[-1]
                self.lower[-1] = temp_max
        
        if len(self.upper) > len(self.lower) + 1:
            self.lower.append(self.upper.pop(0))
            temp_min = min(self.upper)
            if temp_min != self.upper[0]:
                temp_index = self.upper.index(temp_min)
                self.upper[temp_index] = self.upper[0]
                self.upper[0] = temp_min

        #print(self.lower, self.upper)

    def findMedian(self) -> float:
        #print(self.lower, self.upper)
        if (len(self.lower) + len(self.upper)) % 2 == 1:
            if len(self.lower) > len(self.upper):
                return self.lower[-1]
            else:
                return self.upper[0]
        else:
            return (self.lower[-1] + self.upper[0]) / 2
        
        
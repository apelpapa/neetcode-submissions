class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [None] * capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        pushIndex = None
        maxIndex = 0
        for i, value in enumerate(self.arr):
            print(i)
            maxIndex += 1
            if value == None:
                pushIndex = i
                break

        if pushIndex == None:
            self.resize()
            self.arr[maxIndex] = n
        else:
            self.arr[pushIndex] = n
            
    def popback(self) -> int:
        popIndex = self.getSize()-1
        returnValue = self.arr[popIndex]
        self.arr[popIndex] = None
        return returnValue

    def resize(self) -> None:
        past_capacity = self.getCapacity()
        self.arr = [*self.arr] + ([None] * past_capacity)
        self.capacity = len(self.arr)

    def getSize(self) -> int:
        filledCounter = 0
        for i in self.arr:
            if i != None:
                filledCounter += 1

        return filledCounter
        
    def getCapacity(self) -> int:
        return self.capacity

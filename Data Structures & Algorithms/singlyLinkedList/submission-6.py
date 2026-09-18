class LinkedList:
    
    def __init__(self):
        self.ll = list()
        self.length = 0

    def get(self, index: int) -> int:
        if self.checkIndex(index):
            return self.ll[index]
        else:
            return -1   

    def insertHead(self, val: int) -> None:
        self.ll.insert(0, val)
        self.length += 1


    def insertTail(self, val: int) -> None:
        self.ll.append(val)
        self.length += 1

    def remove(self, index: int) -> bool:
        if self.checkIndex(index):
            self.ll.pop(index)
            self.length -= 1
            return True
        else:
            return False

    def getValues(self) -> List[int]:
        return self.ll

    def checkIndex(self, index:int) -> bool:
        if index >= 0 and self.length > 0:
            if index < self.length:
                return True
            else: 
                return False
        else:
            return False

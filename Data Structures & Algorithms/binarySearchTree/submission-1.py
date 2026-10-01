class TreeMap:
    
    def __init__(self):
        self.arr = []
        

    def insert(self, key: int, val: int) -> None:
        print(self.arr)
        if len(self.arr) == 0:
            self.arr.append([key, val])
            return None
        for i, keypair in enumerate(self.arr):
            if self.arr[i][0] == key:
                self.arr[i][1] = val
                return None
        self.arr.append([key, val])
        self.arr.sort()


    def get(self, key: int) -> int:
        for old_key, value in self.arr:
            if old_key == key:
                return value
        
        return -1


    def getMin(self) -> int:
        if self.arr:
            return self.arr[0][1]
        return -1


    def getMax(self) -> int:
        if self.arr:
            return self.arr[-1][1]
        return -1


    def remove(self, key: int) -> None:
        for i, keypair in enumerate(self.arr):
            if self.arr[i][0] == key:
                self.arr.pop(i)

    def getInorderKeys(self) -> List[int]:
        key_list = []
        for key, value in self.arr:
            key_list.append(key)
        return key_list
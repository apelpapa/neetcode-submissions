class LRUCache:

    def __init__(self, capacity: int):
        self.cache = collections.OrderedDict()
        self.capacity = capacity
        self.length = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
        elif self.length < self.capacity:
            self.cache[key] = value
            self.length +=1
        else:
            self.cache.popitem(False)
            self.cache[key] = value

            print("need to kick something")
        

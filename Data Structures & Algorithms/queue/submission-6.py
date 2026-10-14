class ListNode:
    def __init__(self, value, next = None, prev = None):
        self.value = value
        self.prev = prev
        self.next = next        

class Deque:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        if self.head.next == self.tail:
            return True
        return False

    def append(self, value: int) -> None:
        new_node = ListNode(value, self.tail, self.tail.prev)
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        

    def appendleft(self, value: int) -> None:
        new_node = ListNode(value, self.head.next, self.head)
        self.head.next.prev = new_node
        self.head.next = new_node
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        to_pop = self.tail.prev.value
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
        return to_pop
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        to_pop = self.head.next.value
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next
        return to_pop
        

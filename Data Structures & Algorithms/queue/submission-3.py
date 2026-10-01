class ListNode:
    def __init__(self, value, next = None, prev = None):
        self.next = next
        self.prev = prev
        self.value = value

class Deque:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail
        
    def append(self, value: int) -> None:
        new_node = ListNode(value, next=self.tail, prev=self.tail.prev)
        self.tail.prev.next = new_node
        self.tail.prev = new_node
    
    def appendleft(self, value: int) -> None:
        new_node = ListNode(value, next=self.head.next, prev=self.head)
        self.head.next.prev = new_node
        self.head.next = new_node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        node = self.tail.prev
        node.prev.next = self.tail
        self.tail.prev = node.prev
        return node.value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        node = self.head.next
        self.head.next = node.next
        node.next.prev = self.head
        return node.value
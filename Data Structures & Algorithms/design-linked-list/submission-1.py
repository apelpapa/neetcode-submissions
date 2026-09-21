class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
        self.size = 0

    def get(self, index: int) -> int:
        node = self.getNode(index)
        return node.val if node is not None else -1

    def addAtHead(self, val: int) -> None:
        new_head = ListNode(val)
        new_head.next = self.head.next
        new_head.prev = self.head
        if self.head.next is not None:
            self.head.next.prev = new_head
        else:
            self.tail = new_head
        self.head.next = new_head
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_tail = ListNode(val)
        new_tail.prev = self.tail
        self.tail.next = new_tail
        self.tail = new_tail
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return
        next_node = self.getNode(index)
        previous_node = next_node.prev
        new_node = ListNode(val)
        new_node.prev = previous_node
        new_node.next = next_node
        previous_node.next = new_node
        next_node.prev = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        node = self.getNode(index)
        if node is None:
            return
        previous_node = node.prev
        next_node = node.next
        previous_node.next = next_node
        if next_node is not None:
            next_node.prev = previous_node
        else:
            self.tail = previous_node
        self.size -= 1

    def getNode(self, index: int):
        if index < 0 or index >= self.size:
            return None
        current_node = self.head.next
        counter = 0
        while counter < index:
            current_node = current_node.next
            counter += 1
        return current_node

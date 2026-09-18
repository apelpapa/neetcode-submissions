class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        current_node = self.head.next
        i = 0
        while current_node:
            if i == index:
                return current_node.val
            i += 1
            current_node = current_node.next
        return -1

    def insertHead(self, val: int) -> None:
        old_head = self.head.next
        new_head = ListNode(val)
        new_head.next = old_head
        self.head.next = new_head
        
        if old_head is None:
            self.tail = new_head

    def insertTail(self, val: int) -> None:
        new_tail = ListNode(val)
        self.tail.next = new_tail
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        current_node = self.head.next
        previous_node = self.head
        while current_node and i <= index:
            if i == index:
                if current_node.next:
                    previous_node.next = current_node.next
                    return True
                else:
                    previous_node.next = None
                    self.tail = previous_node
                    return True
            i += 1
            previous_node = current_node
            current_node = current_node.next

        return False

    def getValues(self) -> List[int]:
        current_node = self.head.next
        print_array = []
        while current_node:
            print_array.append(current_node.val)
            current_node = current_node.next
        return print_array

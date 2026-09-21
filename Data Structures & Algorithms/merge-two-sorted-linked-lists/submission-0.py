# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merge_list = ListNode()
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1
        if list1.val <= list2.val:
            print("in 1")
            merge_list.val = list1.val
            list1 = list1.next
        else:
            print("in 2")
            merge_list.val = list2.val
            list2 = list2.next
        merge_list_head = merge_list

        while list1 or list2:
            if not list1:
                print("in 3")
                merge_list.next = list2
                merge_list = merge_list.next
                list2 = list2.next
            elif not list2:
                print("in 4")
                merge_list.next = list1
                merge_list = merge_list.next
                list1 = list1.next
            elif list1.val <= list2.val:
                print("in 5")
                merge_list.next = list1
                merge_list = merge_list.next
                list1 = list1.next
            else:
                print("in 6")
                merge_list.next = list2
                merge_list = merge_list.next
                list2 = list2.next
        return merge_list_head

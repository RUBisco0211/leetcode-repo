# leetcode.cn/problems/merge-two-sorted-lists/  (21)
# submission 751544557  accepted 2026-09-26  runtime 0 ms  memory 19.2 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        # 用来保存头结点
        head = ListNode()
        p = head

        while list1 is not None and list2 is not None:
            # 哪个小就先接上哪个，随后该链表指针后移
            if list1.val <= list2.val:
                p.next = list1
                list1 = list1.next
            else:
                p.next = list2
                list2 = list2.next
            # 后移一位指向已经排好的最后一位
            p = p.next
        # p 此时指向其中一个链表尾部，该链表指针指向 None，应该接上另一个链表剩余的部分
        p.next = list1 if list2 is None else list2


        return head.next

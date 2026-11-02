# leetcode.cn/problems/add-two-numbers/  (2)
# submission 751551811  accepted 2026-09-26  runtime 0 ms  memory 19.2 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        # 保存头结点
        head = ListNode()
        p = head

        # 进位
        carry = 0
        while l1 is not None and l2 is not None:
            val = l1.val + l2.val + carry
            p.next = ListNode(val % 10)
            carry = val // 10

            l1 = l1.next
            l2 = l2.next
            p = p.next

        l = l1 if l2 is None else l2
        while l is not None:
            val = l.val + carry
            p.next = ListNode(val % 10)
            carry = val // 10
            l = l.next
            p = p.next
        if carry != 0:
            p.next = ListNode(carry)

        return head.next

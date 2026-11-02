# leetcode.cn/problems/add-two-numbers/  (2)
# submission 751552019  accepted 2026-09-26  runtime 3 ms  memory 19.1 MB

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

        # 位数不一致时需要继续加
        l = l1 if l2 is None else l2

        while l is not None:
            val = l.val + carry
            p.next = ListNode(val % 10)
            carry = val // 10
            l = l.next
            p = p.next
        # 若进位不为0，还需要添加新结点
        if carry != 0:
            p.next = ListNode(carry)

        return head.next

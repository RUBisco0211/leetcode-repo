# leetcode.cn/problems/reverse-linked-list/  (206)
# submission 751481513  accepted 2026-09-26  runtime 0 ms  memory 20.4 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return None
        if head.next is None:
            return head
        
        # 递归法：注意函数语义是：返回反转后的头结点
        p = self.reverseList(head.next)
        # 此时 head 指向 head.next 但 head.next 已经在表尾了，故要把 head.next 和 head 反转
        head.next.next = head
        head.next = None

        return p

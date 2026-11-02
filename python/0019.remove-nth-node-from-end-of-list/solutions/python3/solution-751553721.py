# leetcode.cn/problems/remove-nth-node-from-end-of-list/  (19)
# submission 751553721  accepted 2026-09-26  runtime 0 ms  memory 19.1 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        # 双指针，一个先走 n 步，之后两个一起走，直到先走的到最后一位，则后走的到目标结点前一位

        p = q = head
        for _ in range(n):
            p = p.next
        # 由于 sz >= n，故 p is None 即 sz == n，则倒数第 n 个就是第 head
        if p is None:
            tmp = head.next
            head.next = None
            return tmp

        while p.next is not None:
            p = p.next
            q = q.next
        # 此时 q.next 就是要删除的结点
        q.next = q.next.next

        return head

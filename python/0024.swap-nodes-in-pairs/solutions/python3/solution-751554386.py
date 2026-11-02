# leetcode.cn/problems/swap-nodes-in-pairs/  (24)
# submission 751554386  accepted 2026-09-26  runtime 0 ms  memory 19 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return None
        if head.next is None:
            return head

        p, q = head, head.next
        p.next = self.swapPairs(q.next)
        q.next = p

        return q

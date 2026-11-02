# leetcode.cn/problems/swap-nodes-in-pairs/  (24)
# submission 751554686  accepted 2026-09-26  runtime 0 ms  memory 19.1 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        # 递归最简单
        
        # 先考虑仅有 0 个和 1 个的情况
        if head is None:
            return None
        if head.next is None:
            return head

        # 再考虑至少有两个的情况，交换最前两个结点，并递归交换后面的结点即可
        p, q = head, head.next
        p.next = self.swapPairs(q.next)
        q.next = p

        return q

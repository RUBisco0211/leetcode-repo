# leetcode.cn/problems/intersection-of-two-linked-lists/  (160)
# submission 751458279  accepted 2026-09-26  runtime 122 ms  memory 37.4 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pa, pb = headA, headB

        while pa is not pb:
            pa = pa.next
            pb = pb.next
            if pa is None and pb is None:
                return None
            if pa is None:
                pa = headB
            if pb is None:
                pb = headA
        return pa

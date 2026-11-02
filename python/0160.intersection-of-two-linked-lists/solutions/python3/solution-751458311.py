# leetcode.cn/problems/intersection-of-two-linked-lists/  (160)
# submission 751458311  accepted 2026-09-26  runtime 128 ms  memory 37.4 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pa, pb = headA, headB

        while pa is not pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA

        return pa

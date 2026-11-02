# leetcode.cn/problems/linked-list-cycle/  (141)
# submission 751484955  accepted 2026-09-26  runtime 55 ms  memory 22.4 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        fast, slow = head.next, head
        
        while fast != slow:
            if fast is None or fast.next is None:
               return False
            
            fast = fast.next.next
            slow = slow.next

        return slow == fast

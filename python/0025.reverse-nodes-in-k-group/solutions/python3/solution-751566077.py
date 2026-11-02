# leetcode.cn/problems/reverse-nodes-in-k-group/  (25)
# submission 751566077  accepted 2026-09-26  runtime 7 ms  memory 20.3 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        # 递归

        # 先算长度，这里每一次递归都要做，冗余了吧
        l = 0
        p = head
        while p is not None:
            l += 1
            p = p.next

        # 长度小于 k 直接返回
        if l < k:
            return head
    

        # 长度大于等于 k 的，递归处理

        
        
        curr, nxt = self._reverse(head, k)
        
        head.next = self.reverseKGroup(nxt, k)
        return curr
    
    # 反转一组 k 个结点，返回头结点和下一组待反转的头结点
    def _reverse(self, head: ListNode | None, k: int) -> Tuple[ListNode | None, ListNode | None]:
        cnt = 0
        pre, curr = None, head

        while curr is not None and cnt < k:
            # 已经被反转的部分头是 pre
            # curr 指向要反转的部分的头结点，且已经被反转的部分是游离的
            tmp = curr.next
            curr.next = pre
            pre = curr
            curr = tmp
            cnt += 1
        
        # 反转结束，curr 指向下一组的头，pre 指向当前已经被反转部分的头
        return (pre, curr)

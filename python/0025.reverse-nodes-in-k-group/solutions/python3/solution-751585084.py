# leetcode.cn/problems/reverse-nodes-in-k-group/  (25)
# submission 751585084  accepted 2026-09-26  runtime 4 ms  memory 20.3 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        # 迭代
        if k == 1:
            return head

        l = 0
        p = head
        while p is not None:
            l += 1
            p = p.next

        # 长度小于 k 直接返回
        if l < k:
            return head

        # 分段，保存每一段的起点和终点
        segments = []

        start = end = head
        for _ in range(k - 1):
            end = end.next
        l = k - 1
        while end is not None:
            l += 1
            if l % k == 0:
                segments.append((start, end))
            end = end.next
            start = start.next
        
        # 最后一段如果不足 k，前面的循环没法保存其起终点，需要额外处理
        if l % k != 0:
            _, end = segments[-1]
            start = end.next
            for _ in range(l % k):
                end = end.next
            segments.append((start, end))
        
        # 每一段单独反转
        segs = segments if l % k == 0 else segments[:-1]

        head = segs[0][1] # 新的 head 是第一段的尾结点
        new_end = segs[0][0]

        # 先反转
        for start, end in segs:
            self._reverse(start, end, k)
        
        # 再连接
        for i in range(len(segs) - 1):
            # 新尾连下一段的新头
            segs[i][0].next = segs[i + 1][1]

        # 连上最后一段
        if l % k != 0:
            segs[-1][0].next = segments[-1][0]
        else:
            segs[-1][0].next = None
        
        return head

        


    # 反转一组 k 个结点
    def _reverse(self, start: ListNode, end: ListNode, k: int) -> None:
        curr = start
        stack = []

        # 入栈
        while curr is not end:
            stack.append(curr)
            curr = curr.next

        curr = end
        # 出栈
        while len(stack) > 0:
            top = stack.pop()
            curr.next = top
            curr = top
        curr.next = None

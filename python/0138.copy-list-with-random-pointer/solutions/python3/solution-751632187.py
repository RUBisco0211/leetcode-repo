# leetcode.cn/problems/copy-list-with-random-pointer/  (138)
# submission 751632187  accepted 2026-09-27  runtime 42 ms  memory 19.9 MB

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        p = head
        # 把复制后的结点直接连在原结点后面，之后 random 指向原 random 的下一位即可
        while p is not None:
            if p.next is None:
                p.next = Node(p.val, next=None)
            else:
                tmp = p.next
                p.next = Node(p.val, next=tmp)
            p = p.next.next
        
        # 现在结点数量为偶数了
        # 把新的 randowm 连上
        p = head
        while p is not None:
            p.next.random = p.random.next if p.random is not None else None
            p = p.next.next
        
        # 把两个表分离
        p = head
        new_head = head.next
        while p is not None:
            cpy = p.next
            if cpy.next is None:
                p.next = None
                break
            else:
                nxt = cpy.next
                p.next = cpy.next
                cpy.next = p.next.next
            p = nxt
        
        return new_head

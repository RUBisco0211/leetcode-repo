# leetcode.cn/problems/symmetric-tree/  (101)
# submission 752695360  accepted 2026-10-04  runtime 0 ms  memory 19.4 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if not root:
            return True
        s = [(root.left, root.right)]

        while s:
            match s.pop():
                case (None, None):
                    continue
                case (None, _) | (_, None):
                    return False
                case (p, q):
                    if p.val != q.val:
                        return False
                    s.append((p.left, q.right))
                    s.append((p.right, q.left))
        
        return True

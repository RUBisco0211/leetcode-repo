# leetcode.cn/problems/flatten-binary-tree-to-linked-list/  (114)
# submission 752745547  accepted 2026-10-04  runtime 0 ms  memory 19.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None

        stack = [root]
        # pre 保存先序遍历的前继结点
        pre = None
        
        while stack:
            tmp = stack.pop()
            if pre:
                pre.right = tmp
                pre.left = None
            if tmp.right:
                stack.append(tmp.right)
            if tmp.left:
                stack.append(tmp.left)
            pre = tmp

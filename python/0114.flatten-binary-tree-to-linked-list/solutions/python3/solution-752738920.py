# leetcode.cn/problems/flatten-binary-tree-to-linked-list/  (114)
# submission 752738920  accepted 2026-10-04  runtime 0 ms  memory 19.3 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None | TreeNode:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        
        left_tail = self.flatten(root.left)
        right_tail = self.flatten(root.right)

        if left_tail:
            left_tail.right = root.right
            root.right = root.left
            root.left = None
        return right_tail or left_tail or root

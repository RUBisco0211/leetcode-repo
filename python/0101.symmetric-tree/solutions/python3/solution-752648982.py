# leetcode.cn/problems/symmetric-tree/  (101)
# submission 752648982  accepted 2026-10-03  runtime 0 ms  memory 19.2 MB

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
        if not root.left:
            return root.right is None
        if not root.right:
            return root.left is None
        
        return self._isReversed(root.left, root.right)
        
    def _isReversed(self, left: TreeNode | None, right: TreeNode | None) -> bool:
        if not left:
            return right is None
        if not right:
            return left is None
        if left.val != right.val:
            return False
        return self._isReversed(left.left, right.right) and self._isReversed(left.right, right.left)

# leetcode.cn/problems/maximum-depth-of-binary-tree/  (104)
# submission 752278510  accepted 2026-10-01  runtime 0 ms  memory 22.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        dl = self.maxDepth(root.left)
        dr = self.maxDepth(root.right)
        return max(dl, dr) + 1

# leetcode.cn/problems/validate-binary-search-tree/  (98)
# submission 752727070  accepted 2026-10-04  runtime 0 ms  memory 21 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None, left=-inf, right=inf) -> bool:
        if not root:
            return True 
        x = root.val
        
        return left < x < right \
            and self.isValidBST(root.left, left, x) \
            and self.isValidBST(root.right, x, right)

# leetcode.cn/problems/validate-binary-search-tree/  (98)
# submission 752727883  accepted 2026-10-04  runtime 0 ms  memory 21 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    pre = -inf
    def isValidBST(self, root: TreeNode | None) -> bool:
        if not root:
            return True 
        if not self.isValidBST(root.left):
            return False
        if root.val <= self.pre:
            return False
        self.pre = root.val
        return self.isValidBST(root.right)

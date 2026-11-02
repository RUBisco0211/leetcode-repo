# leetcode.cn/problems/binary-tree-inorder-traversal/  (94)
# submission 752275762  accepted 2026-09-30  runtime 0 ms  memory 19.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []
        l = self.inorderTraversal(root.left)
        r = self.inorderTraversal(root.right)
        return l + [root.val] + r

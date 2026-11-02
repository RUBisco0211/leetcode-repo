# leetcode.cn/problems/diameter-of-binary-tree/  (543)
# submission 752700405  accepted 2026-10-04  runtime 3 ms  memory 21.7 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res: int
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.res = 0
        self._maxDepth(root)

        return self.res
        
    def _maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        dl = self._maxDepth(root.left)
        dr = self._maxDepth(root.right)

        self.res = max(self.res, dl + dr)
        return max(dl, dr) + 1

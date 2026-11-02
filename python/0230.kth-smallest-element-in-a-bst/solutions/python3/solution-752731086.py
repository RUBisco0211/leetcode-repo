# leetcode.cn/problems/kth-smallest-element-in-a-bst/  (230)
# submission 752731086  accepted 2026-10-04  runtime 0 ms  memory 21.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        for val in self._traverse(root):
            cnt += 1
            if cnt == k:
                return val
        
    def _traverse(self, root: TreeNode | None) -> Iterator[int]:
        if root is None:
            return
        yield from self._traverse(root.left)
        yield root.val
        yield from self._traverse(root.right)

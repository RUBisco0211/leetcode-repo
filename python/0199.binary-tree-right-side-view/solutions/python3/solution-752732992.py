# leetcode.cn/problems/binary-tree-right-side-view/  (199)
# submission 752732992  accepted 2026-10-04  runtime 0 ms  memory 19.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res: List[int]
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        self.res = []
        self._dfs(root, 0)
        return self.res

    def _dfs(self, root: TreeNode | None, depth: int):
        if root is None:
            return
        if depth == len(self.res):
            self.res.append(root.val)
        self._dfs(root.right, depth + 1)
        self._dfs(root.left, depth + 1)

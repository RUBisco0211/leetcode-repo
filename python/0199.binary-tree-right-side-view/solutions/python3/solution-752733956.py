# leetcode.cn/problems/binary-tree-right-side-view/  (199)
# submission 752733956  accepted 2026-10-04  runtime 0 ms  memory 19.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []
        stack = [(root, 0)]

        while stack:
            node, depth = stack.pop()
            if depth == len(res):
                res.append(node.val)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

        return res

# leetcode.cn/problems/maximum-depth-of-binary-tree/  (104)
# submission 752279617  accepted 2026-10-01  runtime 3 ms  memory 21.8 MB

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
        # 用栈 DFS，随机次序遍历，结点入栈时记录一下所处高度即可
        stack = [(root, 1)]
        res = 0
        while stack:
            node, d = stack.pop()
            res = max(res, d)
            if node.left:
                stack.append((node.left, d + 1))
            if node.right:
                stack.append((node.right, d + 1))
        
        return res

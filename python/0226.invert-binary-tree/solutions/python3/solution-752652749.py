# leetcode.cn/problems/invert-binary-tree/  (226)
# submission 752652749  accepted 2026-10-03  runtime 0 ms  memory 19.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        q = deque([root])

        while q:
            tmp = q.pop()
            tmp.left, tmp.right = tmp.right, tmp.left

            if tmp.left:
                q.append(tmp.left)
            if tmp.right:
                q.append(tmp.right)
        return root

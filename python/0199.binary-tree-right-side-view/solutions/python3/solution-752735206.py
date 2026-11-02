# leetcode.cn/problems/binary-tree-right-side-view/  (199)
# submission 752735206  accepted 2026-10-04  runtime 0 ms  memory 19.2 MB

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
        q = deque([root])

        while q:
            layer_len = len(q)
            for i in range(layer_len):
                node = q.popleft()
                if i == layer_len - 1:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res

# leetcode.cn/problems/binary-tree-level-order-traversal/  (102)
# submission 752707850  accepted 2026-10-04  runtime 0 ms  memory 19.7 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        q = deque([root])
        res = []

        while q:
            vals = []

            # 每次到这里，q 中节点都是每一层的所有节点
            # 把q中所有节点都依次出队，然后放入其所有子节点
            for _ in range(len(q)):
                node = q.popleft()
                vals.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(vals)
        
        return res

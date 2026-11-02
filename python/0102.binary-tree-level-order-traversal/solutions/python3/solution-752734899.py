# leetcode.cn/problems/binary-tree-level-order-traversal/  (102)
# submission 752734899  accepted 2026-10-04  runtime 0 ms  memory 20 MB

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
            # 需要注意的是，虽然在 for 循环中要向q中插入元素，但 len(q) 只在for循环开始的时候算了一次，是for开始时的长度
            for _ in range(len(q)):
                node = q.popleft()
                vals.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(vals)
        
        return res

# leetcode.cn/problems/maximum-depth-of-binary-tree/  (104)
# submission 752279941  accepted 2026-10-01  runtime 0 ms  memory 21.6 MB

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

        # 队列层序遍历 BFS，走到新的一参就加一
        res = 0
        q = deque([root])

        while q:
            # q 不为空则当前层还有节点
            res += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return res

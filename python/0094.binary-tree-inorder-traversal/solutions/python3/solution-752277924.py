# leetcode.cn/problems/binary-tree-inorder-traversal/  (94)
# submission 752277924  accepted 2026-10-01  runtime 0 ms  memory 19 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        stack = []
        res = []
        node = root
        # 遍历期间 node 可能为 None（找到none就改回头了）但是栈和node都为空的时候才是遍历结束
        while not (len(stack) == 0 and node is None):
            # 不断往左子树走，直到没有左结点
            if node:
                stack.append(node)
                node = node.left
            # 走到空了，就把其父节点（栈顶）元素拿出来记录
            # 然后转向右结点
            else:
                tmp = stack.pop()
                res.append(tmp.val)
                node = tmp.right
            
        return res

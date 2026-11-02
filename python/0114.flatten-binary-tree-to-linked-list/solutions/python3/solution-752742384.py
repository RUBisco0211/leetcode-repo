# leetcode.cn/problems/flatten-binary-tree-to-linked-list/  (114)
# submission 752742384  accepted 2026-10-04  runtime 0 ms  memory 19.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 保存当前链表的头结点
    head: TreeNode | None = None
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None

        # 头插法，先转换右左子树，然后把当前节点right连上head
        self.flatten(root.right) # 此时 head 为 root.right
        self.flatten(root.left) # 此时 head 为 root.left

        root.left = None
        root.right = self.head
        self.head = root

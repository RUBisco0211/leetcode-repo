# leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/  (105)
# submission 752752519  accepted 2026-10-04  runtime 95 ms  memory 89.3 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if len(preorder) == 0 and len(inorder) == 0:
            return None

        val = preorder[0]
        index = inorder.index(val)

        left_inorder = inorder[:index]
        left_preorder = preorder[1:1 + len(left_inorder)]
        
        right_inorder = inorder[index + 1:]
        right_preorder = preorder[1 + len(left_inorder):]

        node = TreeNode(val)
        node.left = self.buildTree(left_preorder, left_inorder)
        node.right = self.buildTree(right_preorder, right_inorder)

        return node

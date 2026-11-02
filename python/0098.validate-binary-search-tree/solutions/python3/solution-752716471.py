# leetcode.cn/problems/validate-binary-search-tree/  (98)
# submission 752716471  accepted 2026-10-04  runtime 7 ms  memory 20.9 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        if not root:
            return True 
        lst = self._traverse(root, order="in")

        for i in range(len(lst) - 1):
            if lst[i] >= lst[i + 1]:
                return False
        
        return True


    def _traverse(self, root: TreeNode | None, order: "in" | "pre" | "post" = "in") -> list[int]:
        if root is None:
            return []
        match order:
            case 'in':
                return self._traverse(root.left) + [root.val] + self._traverse(root.right)
            case 'pre':
                return [root.val] + self._traverse(root.left) + self._traverse(root.right)
            case 'post':
                return self._traverse(root.left) + self._traverse(root.right) + [root.val]

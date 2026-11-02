# leetcode.cn/problems/validate-binary-search-tree/  (98)
# submission 752718159  accepted 2026-10-04  runtime 0 ms  memory 20.6 MB

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
        lst = self._traverse(root)

        for i in range(len(lst) - 1):
            if lst[i] >= lst[i + 1]:
                return False
        
        return True


    def _traverse(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []
        curr = root
        stack = []
        res = []
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                tmp = stack.pop()
                res.append(tmp.val)
                curr = tmp.right
            
        return res

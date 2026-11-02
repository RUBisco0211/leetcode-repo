# leetcode.cn/problems/kth-smallest-element-in-a-bst/  (230)
# submission 752729751  accepted 2026-10-04  runtime 0 ms  memory 21.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res: list[int]
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = []
        stack = []
        curr = root 
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                tmp = stack.pop()
                self.res.append(tmp.val)
                if len(self.res) == k:
                    return self.res[-1]
                curr = tmp.right

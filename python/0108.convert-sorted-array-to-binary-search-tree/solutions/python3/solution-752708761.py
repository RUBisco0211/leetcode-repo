# leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/  (108)
# submission 752708761  accepted 2026-10-04  runtime 3 ms  memory 19.9 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        if len(nums) == 0:
            return None
        
        i = len(nums) // 2
        node = TreeNode(val=nums[i])
        node.left = self.sortedArrayToBST(nums[:i])
        node.right = self.sortedArrayToBST(nums[i + 1:])
        return node

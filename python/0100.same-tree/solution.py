# Created by RUBisco0211 at 2026/11/02 20:12
# leetgo: 1.5.2
# https://leetcode.cn/problems/same-tree/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    p: TreeNode = deserialize("TreeNode", read_line())
    q: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().isSameTree(p, q)
    print("\noutput:", serialize(ans, "boolean"))

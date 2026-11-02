# Created by RUBisco0211 at 2026/11/02 19:59
# leetgo: 1.5.2
# https://leetcode.cn/problems/next-permutation/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    Solution().nextPermutation(nums)
    ans = nums
    print("\noutput:", serialize(ans, "List[int]"))

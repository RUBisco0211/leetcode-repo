# Created by RUBisco0211 at 2026/11/02 20:11
# leetgo: 1.5.2
# https://leetcode.cn/problems/4sum/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().fourSum(nums, target)
    print("\noutput:", serialize(ans, "integer[][]"))

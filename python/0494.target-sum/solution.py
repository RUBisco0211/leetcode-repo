# Created by RUBisco0211 at 2026/11/02 20:13
# leetgo: 1.5.2
# https://leetcode.cn/problems/target-sum/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().findTargetSumWays(nums, target)
    print("\noutput:", serialize(ans, "integer"))

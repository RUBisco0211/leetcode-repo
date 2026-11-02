# Created by RUBisco0211 at 2026/11/02 19:59
# leetgo: 1.5.2
# https://leetcode.cn/problems/partition-equal-subset-sum/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().canPartition(nums)
    print("\noutput:", serialize(ans, "boolean"))

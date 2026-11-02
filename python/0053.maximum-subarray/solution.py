# Created by RUBisco0211 at 2026/11/02 19:58
# leetgo: 1.5.2
# https://leetcode.cn/problems/maximum-subarray/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxSubArray(nums)
    print("\noutput:", serialize(ans, "integer"))

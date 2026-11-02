# Created by RUBisco0211 at 2026/11/02 20:13
# leetgo: 1.5.2
# https://leetcode.cn/problems/min-cost-climbing-stairs/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    cost: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minCostClimbingStairs(cost)
    print("\noutput:", serialize(ans, "integer"))

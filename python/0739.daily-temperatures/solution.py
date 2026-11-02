# Created by RUBisco0211 at 2026/11/02 19:59
# leetgo: 1.5.2
# https://leetcode.cn/problems/daily-temperatures/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        

# @lc code=end

if __name__ == "__main__":
    temperatures: List[int] = deserialize("List[int]", read_line())
    ans = Solution().dailyTemperatures(temperatures)
    print("\noutput:", serialize(ans, "integer[]"))

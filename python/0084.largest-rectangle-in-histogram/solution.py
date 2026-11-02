# Created by RUBisco0211 at 2026/11/02 19:59
# leetgo: 1.5.2
# https://leetcode.cn/problems/largest-rectangle-in-histogram/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    heights: List[int] = deserialize("List[int]", read_line())
    ans = Solution().largestRectangleArea(heights)
    print("\noutput:", serialize(ans, "integer"))

# Created by RUBisco0211 at 2026/11/02 20:12
# leetgo: 1.5.2
# https://leetcode.cn/problems/triangle/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    triangle: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minimumTotal(triangle)
    print("\noutput:", serialize(ans, "integer"))

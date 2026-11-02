# Created by RUBisco0211 at 2026/11/02 19:59
# leetgo: 1.5.2
# https://leetcode.cn/problems/minimum-path-sum/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minPathSum(grid)
    print("\noutput:", serialize(ans, "integer"))

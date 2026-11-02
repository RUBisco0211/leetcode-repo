# Created by RUBisco0211 at 2026/11/02 19:58
# leetgo: 1.5.2
# https://leetcode.cn/problems/rotting-oranges/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().orangesRotting(grid)
    print("\noutput:", serialize(ans, "integer"))

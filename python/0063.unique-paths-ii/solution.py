# Created by RUBisco0211 at 2026/11/02 20:11
# leetgo: 1.5.2
# https://leetcode.cn/problems/unique-paths-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    obstacleGrid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().uniquePathsWithObstacles(obstacleGrid)
    print("\noutput:", serialize(ans, "integer"))

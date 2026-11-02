# Created by RUBisco0211 at 2026/11/02 20:12
# leetgo: 1.5.2
# https://leetcode.cn/problems/maximal-square/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    matrix: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().maximalSquare(matrix)
    print("\noutput:", serialize(ans, "integer"))

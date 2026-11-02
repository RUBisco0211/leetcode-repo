# Created by RUBisco0211 at 2026/11/02 19:58
# leetgo: 1.5.2
# https://leetcode.cn/problems/spiral-matrix/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        

# @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().spiralOrder(matrix)
    print("\noutput:", serialize(ans, "integer[]"))

# Created by RUBisco0211 at 2026/11/02 20:11
# leetgo: 1.5.2
# https://leetcode.cn/problems/spiral-matrix-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().generateMatrix(n)
    print("\noutput:", serialize(ans, "integer[][]"))

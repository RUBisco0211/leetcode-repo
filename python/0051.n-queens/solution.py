# Created by RUBisco0211 at 2026/11/02 19:58
# leetgo: 1.5.2
# https://leetcode.cn/problems/n-queens/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().solveNQueens(n)
    print("\noutput:", serialize(ans, "string[][]"))

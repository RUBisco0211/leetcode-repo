# Created by RUBisco0211 at 2026/11/02 19:59
# leetgo: 1.5.2
# https://leetcode.cn/problems/unique-paths/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    m: int = deserialize("int", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().uniquePaths(m, n)
    print("\noutput:", serialize(ans, "integer"))

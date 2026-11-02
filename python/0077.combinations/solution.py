# Created by RUBisco0211 at 2026/11/02 20:12
# leetgo: 1.5.2
# https://leetcode.cn/problems/combinations/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().combine(n, k)
    print("\noutput:", serialize(ans, "integer[][]"))

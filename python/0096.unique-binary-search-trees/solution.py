# Created by RUBisco0211 at 2026/11/02 20:12
# leetgo: 1.5.2
# https://leetcode.cn/problems/unique-binary-search-trees/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numTrees(self, n: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().numTrees(n)
    print("\noutput:", serialize(ans, "integer"))

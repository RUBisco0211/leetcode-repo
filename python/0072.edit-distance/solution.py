# Created by RUBisco0211 at 2026/11/02 19:59
# leetgo: 1.5.2
# https://leetcode.cn/problems/edit-distance/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    word1: str = deserialize("str", read_line())
    word2: str = deserialize("str", read_line())
    ans = Solution().minDistance(word1, word2)
    print("\noutput:", serialize(ans, "integer"))

# Created by RUBisco0211 at 2026/11/02 20:11
# leetgo: 1.5.2
# https://leetcode.cn/problems/roman-to-integer/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def romanToInt(self, s: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().romanToInt(s)
    print("\noutput:", serialize(ans, "integer"))

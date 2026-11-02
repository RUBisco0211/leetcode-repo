# Created by RUBisco0211 at 2026/11/02 20:12
# leetgo: 1.5.2
# https://leetcode.cn/problems/isomorphic-strings/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    t: str = deserialize("str", read_line())
    ans = Solution().isIsomorphic(s, t)
    print("\noutput:", serialize(ans, "boolean"))

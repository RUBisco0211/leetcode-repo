# Created by RUBisco0211 at 2026/11/02 19:58
# leetgo: 1.5.2
# https://leetcode.cn/problems/minimum-window-substring/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    t: str = deserialize("str", read_line())
    ans = Solution().minWindow(s, t)
    print("\noutput:", serialize(ans, "string"))

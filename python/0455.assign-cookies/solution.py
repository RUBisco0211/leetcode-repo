# Created by RUBisco0211 at 2026/11/02 20:13
# leetgo: 1.5.2
# https://leetcode.cn/problems/assign-cookies/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    g: List[int] = deserialize("List[int]", read_line())
    s: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findContentChildren(g, s)
    print("\noutput:", serialize(ans, "integer"))

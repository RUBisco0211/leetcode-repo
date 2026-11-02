# Created by RUBisco0211 at 2026/11/02 20:11
# leetgo: 1.5.2
# https://leetcode.cn/problems/longest-common-prefix/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        

# @lc code=end

if __name__ == "__main__":
    strs: List[str] = deserialize("List[str]", read_line())
    ans = Solution().longestCommonPrefix(strs)
    print("\noutput:", serialize(ans, "string"))

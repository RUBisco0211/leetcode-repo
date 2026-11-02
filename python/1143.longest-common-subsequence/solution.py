# Created by RUBisco0211 at 2026/11/02 19:59
# leetgo: 1.5.2
# https://leetcode.cn/problems/longest-common-subsequence/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    text1: str = deserialize("str", read_line())
    text2: str = deserialize("str", read_line())
    ans = Solution().longestCommonSubsequence(text1, text2)
    print("\noutput:", serialize(ans, "integer"))

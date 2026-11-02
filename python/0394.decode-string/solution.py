# Created by RUBisco0211 at 2026/11/02 19:59
# leetgo: 1.5.2
# https://leetcode.cn/problems/decode-string/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def decodeString(self, s: str) -> str:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().decodeString(s)
    print("\noutput:", serialize(ans, "string"))

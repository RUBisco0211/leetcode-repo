# Created by RUBisco0211 at 2026/11/02 20:11
# leetgo: 1.5.2
# https://leetcode.cn/problems/integer-to-roman/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def intToRoman(self, num: int) -> str:
        

# @lc code=end

if __name__ == "__main__":
    num: int = deserialize("int", read_line())
    ans = Solution().intToRoman(num)
    print("\noutput:", serialize(ans, "string"))

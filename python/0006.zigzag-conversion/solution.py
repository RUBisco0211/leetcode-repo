# Created by RUBisco0211 at 2026/11/02 20:11
# leetgo: 1.5.2
# https://leetcode.cn/problems/zigzag-conversion/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    numRows: int = deserialize("int", read_line())
    ans = Solution().convert(s, numRows)
    print("\noutput:", serialize(ans, "string"))

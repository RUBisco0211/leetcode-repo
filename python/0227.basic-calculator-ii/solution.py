# Created by RUBisco0211 at 2026/11/02 20:12
# leetgo: 1.5.2
# https://leetcode.cn/problems/basic-calculator-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def calculate(self, s: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().calculate(s)
    print("\noutput:", serialize(ans, "integer"))

# Created by RUBisco0211 at 2026/11/02 20:13
# leetgo: 1.5.2
# https://leetcode.cn/problems/lemonade-change/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    bills: List[int] = deserialize("List[int]", read_line())
    ans = Solution().lemonadeChange(bills)
    print("\noutput:", serialize(ans, "boolean"))

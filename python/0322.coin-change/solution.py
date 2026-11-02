# Created by RUBisco0211 at 2026/11/02 19:59
# leetgo: 1.5.2
# https://leetcode.cn/problems/coin-change/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    coins: List[int] = deserialize("List[int]", read_line())
    amount: int = deserialize("int", read_line())
    ans = Solution().coinChange(coins, amount)
    print("\noutput:", serialize(ans, "integer"))

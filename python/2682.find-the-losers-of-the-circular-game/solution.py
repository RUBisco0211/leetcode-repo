# Created by RUBisco0211 at 2026/11/02 20:13
# leetgo: 1.5.2
# https://leetcode.cn/problems/find-the-losers-of-the-circular-game/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().circularGameLosers(n, k)
    print("\noutput:", serialize(ans, "integer[]"))

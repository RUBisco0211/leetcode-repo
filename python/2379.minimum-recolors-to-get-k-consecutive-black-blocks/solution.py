# Created by RUBisco0211 at 2026/11/02 20:13
# leetgo: 1.5.2
# https://leetcode.cn/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    blocks: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minimumRecolors(blocks, k)
    print("\noutput:", serialize(ans, "integer"))

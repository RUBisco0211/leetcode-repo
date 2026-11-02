# Created by RUBisco0211 at 2026/11/02 20:11
# leetgo: 1.5.2
# https://leetcode.cn/problems/plus-one/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        

# @lc code=end

if __name__ == "__main__":
    digits: List[int] = deserialize("List[int]", read_line())
    ans = Solution().plusOne(digits)
    print("\noutput:", serialize(ans, "integer[]"))

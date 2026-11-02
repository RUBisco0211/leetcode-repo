# Created by RUBisco0211 at 2026/11/02 19:58
# leetgo: 1.5.2
# https://leetcode.cn/problems/letter-combinations-of-a-phone-number/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        

# @lc code=end

if __name__ == "__main__":
    digits: str = deserialize("str", read_line())
    ans = Solution().letterCombinations(digits)
    print("\noutput:", serialize(ans, "string[]"))

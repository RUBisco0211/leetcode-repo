# Created by RUBisco0211 at 2026/11/02 20:12
# leetgo: 1.5.2
# https://leetcode.cn/problems/evaluate-reverse-polish-notation/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    tokens: List[str] = deserialize("List[str]", read_line())
    ans = Solution().evalRPN(tokens)
    print("\noutput:", serialize(ans, "integer"))

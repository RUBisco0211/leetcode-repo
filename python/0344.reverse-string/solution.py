# Created by RUBisco0211 at 2026/11/02 20:13
# leetgo: 1.5.2
# https://leetcode.cn/problems/reverse-string/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        

# @lc code=end

if __name__ == "__main__":
    s: List[str] = deserialize("List[str]", read_line())
    Solution().reverseString(s)
    ans = s
    print("\noutput:", serialize(ans, "List[str]"))

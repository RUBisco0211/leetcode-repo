# Created by RUBisco0211 at 2026/11/02 20:11
# leetgo: 1.5.2
# https://leetcode.cn/problems/palindrome-number/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isPalindrome(self, x: int) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    x: int = deserialize("int", read_line())
    ans = Solution().isPalindrome(x)
    print("\noutput:", serialize(ans, "boolean"))

# Created by RUBisco0211 at 2026/11/02 20:13
# leetgo: 1.5.2
# https://leetcode.cn/problems/valid-anagram/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    t: str = deserialize("str", read_line())
    ans = Solution().isAnagram(s, t)
    print("\noutput:", serialize(ans, "boolean"))

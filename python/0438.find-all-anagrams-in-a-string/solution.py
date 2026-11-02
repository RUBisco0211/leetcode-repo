# Created by RUBisco0211 at 2026/11/02 19:58
# leetgo: 1.5.2
# https://leetcode.cn/problems/find-all-anagrams-in-a-string/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    p: str = deserialize("str", read_line())
    ans = Solution().findAnagrams(s, p)
    print("\noutput:", serialize(ans, "integer[]"))

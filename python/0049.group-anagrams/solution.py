# Created by RUBisco0211 at 2026/11/02 19:58
# leetgo: 1.5.2
# https://leetcode.cn/problems/group-anagrams/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        

# @lc code=end

if __name__ == "__main__":
    strs: List[str] = deserialize("List[str]", read_line())
    ans = Solution().groupAnagrams(strs)
    print("\noutput:", serialize(ans, "string[][]"))

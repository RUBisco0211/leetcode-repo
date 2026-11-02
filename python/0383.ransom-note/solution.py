# Created by RUBisco0211 at 2026/11/02 20:13
# leetgo: 1.5.2
# https://leetcode.cn/problems/ransom-note/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    ransomNote: str = deserialize("str", read_line())
    magazine: str = deserialize("str", read_line())
    ans = Solution().canConstruct(ransomNote, magazine)
    print("\noutput:", serialize(ans, "boolean"))

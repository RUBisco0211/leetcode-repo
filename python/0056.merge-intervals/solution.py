# Created by RUBisco0211 at 2026/11/02 19:58
# leetgo: 1.5.2
# https://leetcode.cn/problems/merge-intervals/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        

# @lc code=end

if __name__ == "__main__":
    intervals: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().merge(intervals)
    print("\noutput:", serialize(ans, "integer[][]"))

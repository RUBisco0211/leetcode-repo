# Created by RUBisco0211 at 2026/11/02 20:12
# leetgo: 1.5.2
# https://leetcode.cn/problems/contains-duplicate/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().containsDuplicate(nums)
    print("\noutput:", serialize(ans, "boolean"))

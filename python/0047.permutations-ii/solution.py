# Created by RUBisco0211 at 2026/11/02 20:11
# leetgo: 1.5.2
# https://leetcode.cn/problems/permutations-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().permuteUnique(nums)
    print("\noutput:", serialize(ans, "integer[][]"))

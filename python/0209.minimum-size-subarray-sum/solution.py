# Created by RUBisco0211 at 2026/11/02 20:12
# leetgo: 1.5.2
# https://leetcode.cn/problems/minimum-size-subarray-sum/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    target: int = deserialize("int", read_line())
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minSubArrayLen(target, nums)
    print("\noutput:", serialize(ans, "integer"))

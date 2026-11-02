# Created by RUBisco0211 at 2026/11/02 20:13
# leetgo: 1.5.2
# https://leetcode.cn/problems/maximum-average-subarray-i/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().findMaxAverage(nums, k)
    print("\noutput:", serialize(ans, "double"))

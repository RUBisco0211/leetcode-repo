# Created by RUBisco0211 at 2026/11/02 19:58
# leetgo: 1.5.2
# https://leetcode.cn/problems/subarray-sum-equals-k/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().subarraySum(nums, k)
    print("\noutput:", serialize(ans, "integer"))

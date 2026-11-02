# Created by RUBisco0211 at 2026/11/02 20:13
# leetgo: 1.5.2
# https://leetcode.cn/problems/maximum-length-of-repeated-subarray/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findLength(nums1, nums2)
    print("\noutput:", serialize(ans, "integer"))

# Created by RUBisco0211 at 2026/11/02 19:59
# leetgo: 1.5.2
# https://leetcode.cn/problems/median-of-two-sorted-arrays/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        

# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findMedianSortedArrays(nums1, nums2)
    print("\noutput:", serialize(ans, "double"))

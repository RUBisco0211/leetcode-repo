# Created by RUBisco0211 at 2026/11/02 20:12
# leetgo: 1.5.2
# https://leetcode.cn/problems/merge-sorted-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        

# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    m: int = deserialize("int", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    n: int = deserialize("int", read_line())
    Solution().merge(nums1, m, nums2, n)
    ans = nums1
    print("\noutput:", serialize(ans, "List[int]"))

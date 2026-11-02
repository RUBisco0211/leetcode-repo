# Created by RUBisco0211 at 2026/11/02 19:59
# leetgo: 1.5.2
# https://leetcode.cn/problems/kth-largest-element-in-an-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().findKthLargest(nums, k)
    print("\noutput:", serialize(ans, "integer"))

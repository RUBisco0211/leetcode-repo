# Created by RUBisco0211 at 2026/11/02 20:11
# leetgo: 1.5.2
# https://leetcode.cn/problems/remove-element/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    val: int = deserialize("int", read_line())
    ans = Solution().removeElement(nums, val)
    print("\noutput:", serialize(ans, "integer"))

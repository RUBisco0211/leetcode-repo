# Created by RUBisco0211 at 2026/11/02 20:12
# leetgo: 1.5.2
# https://leetcode.cn/problems/combination-sum-iii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    k: int = deserialize("int", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().combinationSum3(k, n)
    print("\noutput:", serialize(ans, "integer[][]"))

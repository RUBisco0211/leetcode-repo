# Created by RUBisco0211 at 2026/11/02 21:02
# leetgo: 1.5.2
# https://leetcode.cn/problems/permutation-ii-lcci/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def permutation(self, S: str) -> List[str]:
        

# @lc code=end

if __name__ == "__main__":
    S: str = deserialize("str", read_line())
    ans = Solution().permutation(S)
    print("\noutput:", serialize(ans, "string[]"))

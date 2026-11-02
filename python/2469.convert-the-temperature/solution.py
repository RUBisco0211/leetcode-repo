# Created by RUBisco0211 at 2026/11/02 20:13
# leetgo: 1.5.2
# https://leetcode.cn/problems/convert-the-temperature/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        

# @lc code=end

if __name__ == "__main__":
    celsius: float = deserialize("float", read_line())
    ans = Solution().convertTemperature(celsius)
    print("\noutput:", serialize(ans, "double[]"))

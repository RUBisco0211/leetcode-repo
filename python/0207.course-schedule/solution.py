# Created by RUBisco0211 at 2026/11/02 19:58
# leetgo: 1.5.2
# https://leetcode.cn/problems/course-schedule/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    numCourses: int = deserialize("int", read_line())
    prerequisites: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().canFinish(numCourses, prerequisites)
    print("\noutput:", serialize(ans, "boolean"))

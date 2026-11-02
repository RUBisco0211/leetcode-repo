# Created by RUBisco0211 at 2026/11/02 20:11
# leetgo: 1.5.2
# https://leetcode.cn/problems/sudoku-solver/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        

# @lc code=end

if __name__ == "__main__":
    board: List[List[str]] = deserialize("List[List[str]]", read_line())
    Solution().solveSudoku(board)
    ans = board
    print("\noutput:", serialize(ans, "List[List[str]]"))

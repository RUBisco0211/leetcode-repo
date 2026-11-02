# leetcode.cn/problems/pascals-triangle/  (118)
# submission 751686591  accepted 2026-09-27  runtime 0 ms  memory 19.3 MB

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = [[1] * (i + 1) for i in range(numRows)]

        for i in range(2, numRows):
            for j in range(1, i):
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
        
        return res

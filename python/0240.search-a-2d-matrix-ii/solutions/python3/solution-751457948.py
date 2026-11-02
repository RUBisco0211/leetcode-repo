# leetcode.cn/problems/search-a-2d-matrix-ii/  (240)
# submission 751457948  accepted 2026-09-26  runtime 153 ms  memory 25.3 MB

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        steps = 0
        # 从右上角开始搜索，如果当前值偏小，就向下；如果当前值偏大，就向左
        i, j = 0, n - 1
        while i < m and j >= 0:
            value = matrix[i][j]
            if value == target:
                return True
            elif value < target:
                i += 1
            else:
                j -= 1
        
        return False

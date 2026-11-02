# leetcode.cn/problems/search-a-2d-matrix/  (74)
# submission 752871265  accepted 2026-10-05  runtime 0 ms  memory 19.4 MB

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = (left + right) // 2
            i, j = mid // n, mid % n
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

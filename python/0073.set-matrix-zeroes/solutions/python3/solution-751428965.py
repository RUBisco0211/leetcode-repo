# leetcode.cn/problems/set-matrix-zeroes/  (73)
# submission 751428965  accepted 2026-09-25  runtime 12 ms  memory 20.6 MB

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows = set()
        cols = set()

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        for i in rows:
            for j in range(n):
                matrix[i][j] = 0
        
        for j in cols:
            for i in range(m):
                matrix[i][j] = 0

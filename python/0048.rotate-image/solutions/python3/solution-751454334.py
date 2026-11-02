# leetcode.cn/problems/rotate-image/  (48)
# submission 751454334  accepted 2026-09-26  runtime 0 ms  memory 18.9 MB

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # 按主对角线转置一次，再沿中线交换左右列

        n = len(matrix)

        # 转置
        for i in range(1, n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # 沿中线交换左右列
        for j in range(n // 2):
            for i in range(n):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]

# leetcode.cn/problems/set-matrix-zeroes/  (73)
# submission 751447557  accepted 2026-09-25  runtime 3 ms  memory 20.8 MB

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        n = len(matrix[0])

        # 记录原始状态第零行和第零列是否有 0 
        row0_has_0 = 0 in matrix[0]
        col0_has_0 = any([row[0] == 0 for row in matrix])
            
        # 遍历时跳过第零行和第零列
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    # 某一元素为 0，就把它所在的行列索引在第零行和第零列标记出来
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                # 检查每个元素相应的索引是否被标记
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # 最后处理开始的第零行和第零列
        if row0_has_0:
            for j in range(n):
                matrix[0][j] = 0

        if col0_has_0:
            for row in matrix:
                row[0] = 0

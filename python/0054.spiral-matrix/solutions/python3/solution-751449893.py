# leetcode.cn/problems/spiral-matrix/  (54)
# submission 751449893  accepted 2026-09-25  runtime 0 ms  memory 19.2 MB

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        # 方向轮转：右下左上，用数组方便转向，索引 +1 对 4 取模即可
        DIRS = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        ]

        m = len(matrix)
        n = len(matrix[0])

        res = []

        i, j = 0, 0
        dir_index = 0 # 方向索引，初始时向右
        for _ in range(m * n):
            res.append(matrix[i][j])
            # 访问过立即标记
            matrix[i][j] = None
            # 当前方向，以及下一步的可能位置
            di, dj = DIRS[dir_index]
            tmp_i, tmp_j = i + di, j + dj

            # 若按原来的方向会导致出界或走到已经访问的位置，就顺延转向 90 度
            if tmp_i < 0 or tmp_i >= m or tmp_j < 0 or tmp_j >= n or matrix[tmp_i][tmp_j] is None:
                dir_index = (dir_index + 1) % 4
            di, dj = DIRS[dir_index]
            i += di
            j += dj
        
        return res

# leetcode.cn/problems/rotting-oranges/  (994)
# submission 752275389  accepted 2026-09-30  runtime 0 ms  memory 19.1 MB

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        m = len(grid)
        n = len(grid[0])

        rottens = {(i, j) for i in range(m) for j in range(n) if grid[i][j] == 2}
        freshes = {(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1}

        time = 0

        while freshes:
            # 上一轮没有新鲜变腐烂的橘子
            if not rottens:
                return -1
            # 由新鲜变腐烂的橘子
            rottens = {
                (i + di, j + dj) 
                for i, j in rottens 
                for di, dj in DIRECTIONS 
                if (i + di, j + dj) in freshes
            }
            # freshes 排除掉这一轮腐烂的橘子
            freshes -= rottens
            time += 1
        return time

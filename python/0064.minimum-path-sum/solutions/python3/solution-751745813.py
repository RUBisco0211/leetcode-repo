# leetcode.cn/problems/minimum-path-sum/  (64)
# submission 751745813  accepted 2026-09-27  runtime 7 ms  memory 21.4 MB

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        if m == 1:
            return sum(grid[0])
        if n == 1:
            return sum([grid[i][0] for i in range(m)])

        dp = [[0] * n for _ in range(m)]

        s = 0
        for i in range(m):
            s += grid[i][0]
            dp[i][0] = s
        
        s = 0
        for j in range(n):
            s += grid[0][j]
            dp[0][j] = s

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[-1][-1]

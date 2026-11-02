# leetcode.cn/problems/unique-paths/  (62)
# submission 751742725  accepted 2026-09-27  runtime 0 ms  memory 19.1 MB

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        dp = [[1] * n] * m
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[-1][-1]

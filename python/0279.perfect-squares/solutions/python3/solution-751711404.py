# leetcode.cn/problems/perfect-squares/  (279)
# submission 751711404  accepted 2026-09-27  runtime 1487 ms  memory 19.4 MB

class Solution:
    def numSquares(self, n: int) -> int:
        squares = []

        for i in range(1, int(n ** 0.5) + 1):
            squares.append(i ** 2)
        
        dp = [i for i in range(n + 1)]

        for i in range(1, n + 1):
            for sq in squares:
                if sq <= i:
                    dp[i] = min(dp[i], dp[i - sq] + 1)
                else:
                    break
        
        return dp[-1]

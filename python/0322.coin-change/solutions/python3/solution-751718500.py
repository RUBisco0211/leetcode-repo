# leetcode.cn/problems/coin-change/  (322)
# submission 751718500  accepted 2026-09-27  runtime 493 ms  memory 19.6 MB

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # dp[i] 表示凑成 i 最少的硬币个数，初始化为 i + 1，若最后还是 n + 1 说明没有找到可行组合
        dp = [amount + 1 for i in range(amount + 1)]
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[-1] if dp[-1] <= amount else -1

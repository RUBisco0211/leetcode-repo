# leetcode.cn/problems/edit-distance/  (72)
# submission 751756633  accepted 2026-09-27  runtime 55 ms  memory 22.9 MB

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 列：原字符串，行：新字符串
        # 向下：跳过原字符，即删除
        # 向右：添加新字符
        # 左上到右下：若相同则不用做，不同则替换
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                ch1, ch2 = word1[i - 1], word2[j - 1]
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + (1 if ch1 != ch2 else 0))
        
        return dp[-1][-1]

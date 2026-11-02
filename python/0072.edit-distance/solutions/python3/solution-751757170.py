# leetcode.cn/problems/edit-distance/  (72)
# submission 751757170  accepted 2026-09-27  runtime 51 ms  memory 22.7 MB

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 列：原字符串，行：新字符串
        # 向下：跳过原字符，即删除
        # 向右：添加新字符
        # 左上到右下：若相同则不用做，不同则替换

        # 0 行 / 0 列表示从空到当前前缀串需要的操作次数，只有删除或添加
        for i in range(m + 1): # 删除次数
            dp[i][0] = i
        for j in range(n + 1): # 添加次数
            dp[0][j] = j
        
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                ch1, ch2 = word1[i - 1], word2[j - 1]
                # 删除 / 添加 / 替换（若字符相同则不用做）
                dp[i][j] = min(
                    dp[i - 1][j] + 1, # 删除字符
                    dp[i][j - 1] + 1, # 添加字符
                    dp[i - 1][j - 1] + (1 if ch1 != ch2 else 0) # 替换或不动
                )
        
        return dp[-1][-1]

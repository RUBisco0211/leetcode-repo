# leetcode.cn/problems/word-break/  (139)
# submission 751721908  accepted 2026-09-27  runtime 4 ms  memory 19 MB

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 子问题：dp[i] 表示前缀子串是否能被拆分
        # 对于每个 word, j = i - len(word)
        # dp[i] = dp[j] and s[j:i] == word
        # 且找到一个可行即可提过其余单词
        n = len(s)
        dp = [False] * (n + 1)

        dp[0] = True

        for i in range(1, n + 1):
            for word in wordDict:
                lw = len(word)
                if i < len(word):
                    dp[i] = False
                else:
                    dp[i] = dp[i - lw] and s[i - lw: i] == word
                if dp[i]:
                    break
        
        return dp[-1]

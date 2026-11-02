// leetcode.cn/problems/word-break/  (139)
// submission 465811239  accepted 2023-09-13  runtime 11 ms  memory 42.5 MB

class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        int n = s.length();
        boolean[] dp = new boolean[n + 1];
        dp[0] = true;
        for (int i = 1; i <= n; i++) 
            for (int j = 0; j < i; j++)
                if (dp[j] && wordDict.contains(s.substring(j, i))) {
                    dp[i] = true;
                    break;
                }
        return dp[n];
    }
}

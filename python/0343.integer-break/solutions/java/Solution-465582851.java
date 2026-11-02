// leetcode.cn/problems/integer-break/  (343)
// submission 465582851  accepted 2023-09-12  runtime 1 ms  memory 38.3 MB

class Solution {
    public int integerBreak(int n) {
        int[] dp = new int[n + 1];
        dp[2] = 1;
        for (int i = 3; i < dp.length; i++) 
            for (int j = 1; j < i; j++) 
                dp[i] = Math.max(dp[i], Math.max(dp[i - j] * j, (i - j) * j));
        return dp[n];
    }
}

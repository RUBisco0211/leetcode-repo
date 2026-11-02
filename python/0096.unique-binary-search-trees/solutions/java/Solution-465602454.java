// leetcode.cn/problems/unique-binary-search-trees/  (96)
// submission 465602454  accepted 2023-09-12  runtime 0 ms  memory 37.9 MB

class Solution {
    public int numTrees(int n) {
        int[] dp = new int[n + 1];
        dp[0] = 1;
        for (int i = 1; i <= n; i++)
            for (int j = 0; j <= i - 1; j++)
                dp[i] += (dp[j] * dp[i - j - 1]);
        return dp[n];
    }
}

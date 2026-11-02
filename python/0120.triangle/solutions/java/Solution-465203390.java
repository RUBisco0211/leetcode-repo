// leetcode.cn/problems/triangle/  (120)
// submission 465203390  accepted 2023-09-11  runtime 3 ms  memory 42.8 MB

class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int n = triangle.size();
        int[][] dp = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                int value = triangle.get(i).get(j);
                if (i == 0)
                    dp[i][j] = value;
                else if (j == 0)
                    dp[i][j] = dp[i - 1][j] + value;
                else if (i == j)
                    dp[i][j] = dp[i - 1][j - 1] + value;
                else
                    dp[i][j] = Math.min(dp[i - 1][j - 1], dp[i - 1][j]) + value;
            }
            
        }
        int min = dp[n - 1][0];
        for (int j = 0; j < n; j++)
            if (dp[n - 1][j] < min)
                min = dp[n - 1][j];
        return min;
    }
}

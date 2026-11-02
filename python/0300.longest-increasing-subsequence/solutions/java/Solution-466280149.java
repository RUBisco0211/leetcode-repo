// leetcode.cn/problems/longest-increasing-subsequence/  (300)
// submission 466280149  accepted 2023-09-14  runtime 63 ms  memory 41.9 MB

class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] dp = new int[nums.length];
        dp[0] = 1;
        for (int i = 1; i < nums.length; i++) {
            dp[i] = 1;
            for (int j = 0; j < i; j++)
                if (nums[j] < nums[i])
                    dp[i] = Math.max(dp[i], dp[j] + 1);
        }
        int max = 1;
        for (int i = 0; i < nums.length; i++)
            max = Math.max(max, dp[i]);
        return max;
    }
}

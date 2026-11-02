// leetcode.cn/problems/longest-increasing-subsequence/  (300)
// submission 466279369  accepted 2023-09-14  runtime 67 ms  memory 41.8 MB

class Solution {
    public int lengthOfLIS(int[] nums) {
        int max = 1;
        int[] dp = new int[nums.length];
        dp[0] = 1;
        for (int i = 1; i < nums.length; i++) {
            dp[i] = 1;
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i])
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                max = Math.max(max, dp[i]);
            }
        }
        return max;
    }
}

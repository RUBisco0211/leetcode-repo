// leetcode.cn/problems/longest-continuous-increasing-subsequence/  (674)
// submission 466283367  accepted 2023-09-14  runtime 1 ms  memory 42.1 MB

class Solution {
    public int findLengthOfLCIS(int[] nums) {
        int[] dp = new int[nums.length];
        dp[0] = 1;
        int max = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i - 1] < nums[i])
                dp[i] = dp[i - 1] + 1;
            else
                dp[i] = 1;
            max = Math.max(dp[i], max);
        }
        return max;

    }
}

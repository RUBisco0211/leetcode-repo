// leetcode.cn/problems/house-robber/  (198)
// submission 465862990  accepted 2023-09-13  runtime 0 ms  memory 38.7 MB

class Solution {
    public static int rob(int[] nums) {
        int n = nums.length;
        if (n == 0)
            return 0;
        if (n == 1)
            return nums[0];
        if (n == 2)
            return Math.max(nums[0], nums[1]);
        int[] dp = new int[n];
        dp[0] = nums[0];
        dp[1] = nums[1];
        dp[2] = nums[0] + nums[2];
        int max = Math.max(dp[1], dp[2]);
        for (int i = 3; i < n; i++) {
            dp[i] = Math.max(dp[i - 2], dp[i - 3]) + nums[i];
            max = Math.max(dp[i], max);
        }
        return max;
    }
}

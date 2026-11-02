// leetcode.cn/problems/maximum-subarray/  (53)
// submission 704461457  accepted 2026-03-09  runtime 3 ms  memory 77.5 MB

class Solution {
    public int maxSubArray(int[] nums) {
        //      dp[i] 表示以 nums[i] 结尾的最大的子数组和
        int[] dp = new int[nums.length];


        int max = Integer.MIN_VALUE;
        for (int i = 0; i < nums.length; i++) {
            if (i == 0)
                dp[i] = nums[i];
            else
//                继续顺延还是以 nums[i] 作为新的子数组
                dp[i] = Math.max(dp[i - 1] + nums[i], nums[i]);
            max = Math.max(max, dp[i]);
        }
        return max;
    }
}

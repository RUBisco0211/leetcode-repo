// leetcode.cn/problems/longest-increasing-subsequence/  (300)
// submission 419612840  accepted 2023-03-31  runtime 64 ms  memory 40.8 MB

class Solution {
    public int lengthOfLIS(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n];
        int max = 1;
        for(int i=0;i<n;i++)
            dp[i] = 1;

        for(int i=0;i<n;i++){
            for(int j=0;j<i;j++)
                if(nums[j]<nums[i])
                    dp[i] = Math.max(dp[j]+1,dp[i]);
            max = Math.max(max,dp[i]);
        }
        return max;
    }
}

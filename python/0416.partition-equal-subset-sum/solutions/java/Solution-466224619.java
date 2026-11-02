// leetcode.cn/problems/partition-equal-subset-sum/  (416)
// submission 466224619  accepted 2023-09-14  runtime 23 ms  memory 39.7 MB

class Solution {
    public static boolean canPartition(int[] nums) {
        int sum = Arrays.stream(nums).reduce(0, Integer::sum);
        if (sum % 2 != 0)
            return false;
        int n = sum / 2;
        int[] dp = new int[n + 1];
        for (int num: nums)
            for (int i = n; i >= num; i--)
                dp[i] = Math.max(dp[i], num + dp[i - num]);
        return dp[n] == n;
    }
}

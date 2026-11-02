// leetcode.cn/problems/target-sum/  (494)
// submission 466273274  accepted 2023-09-14  runtime 3 ms  memory 39.1 MB

class Solution {
    public static int findTargetSumWays(int[] nums, int target) {
        int sum = Arrays.stream(nums).reduce(0, Integer::sum);
        if ((sum + target) % 2 == 1)
            return 0;
        int plus = (sum + target) / 2;
        int minus = sum - plus;
        int n = plus >= 0 ? plus:minus;
        int[] dp = new int[n + 1];
        dp[0] = 1;
        for (int num: nums)
            for (int i = n; i >= num; i--)
                dp[i] += dp[i - num];
        return dp[n];
    }
}

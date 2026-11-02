// leetcode.cn/problems/jump-game-ii/  (45)
// submission 465617516  accepted 2023-09-12  runtime 272 ms  memory 43.2 MB

class Solution {
    public int jump(int[] nums) {
        int[] dp = new int[nums.length];
        dp[0] = 0;
        for (int i = 1; i < nums.length; i++) {
            dp[i] = Integer.MAX_VALUE;
            for (int j = 0; j < i; j++)
                if (nums[j] + j >= i)
                    dp[i] = Math.min(dp[i], dp[j] + 1);
        }
        return dp[nums.length - 1];
    }
}

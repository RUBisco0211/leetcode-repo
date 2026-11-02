// leetcode.cn/problems/jump-game-ii/  (45)
// submission 465617438  accepted 2023-09-12  runtime 417 ms  memory 42.6 MB

class Solution {
    public int jump(int[] nums) {
        int[] dp = new int[nums.length];
        dp[0] = 0;
        for (int i = 1; i < nums.length; i++) {
            dp[i] = Integer.MAX_VALUE;
            for (int j = 0; j < i; j++)
                if (nums[j] + j >= i)
                    dp[i] = Math.min(dp[i], dp[j] + 1);
            System.out.println(dp[i]);
        }
        return dp[nums.length - 1];
    }
}

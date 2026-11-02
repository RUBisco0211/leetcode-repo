// leetcode.cn/problems/coin-change/  (322)
// submission 465909654  accepted 2023-09-13  runtime 12 ms  memory 41.8 MB

class Solution {
    public int coinChange(int[] coins, int amount) {
        int n = coins.length;
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, amount + 1);
        // dp[i]的值不会达到amount+1（全用 1 换用最多硬币，也只达到amount）便于后面比较更新dp[i]
        int max = amount + 1;
        dp[0] = 0;
        for (int i = 1; i <= amount; i++)
            for (int coin: coins)
                if (i >= coin)
                    dp[i] = Math.min(dp[i], dp[i - coin] + 1);
        return dp[amount] > amount ? -1: dp[amount];
    }
}

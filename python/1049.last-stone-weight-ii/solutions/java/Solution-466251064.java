// leetcode.cn/problems/last-stone-weight-ii/  (1049)
// submission 466251064  accepted 2023-09-14  runtime 3 ms  memory 38.8 MB

class Solution {
    public int lastStoneWeightII(int[] stones) {
        int sum = Arrays.stream(stones).reduce(0, Integer::sum);
        int n = sum / 2;
        int[] dp = new int[n + 1];
        for (int stone: stones)
            for (int i = n; i >= stone; i--)
                dp[i] = Math.max(dp[i], dp[i - stone] + stone);
        return sum - 2 * dp[n];
    }
}

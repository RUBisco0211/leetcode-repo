// leetcode.cn/problems/perfect-squares/  (279)
// submission 465916899  accepted 2023-09-13  runtime 418 ms  memory 42.2 MB

class Solution {
    public int numSquares(int n) {
        //  获取比 n 小的完全平方数
        List<Integer> squares = new ArrayList();
        for (int i = 1; i <= Math.sqrt(n); i++)
            squares.add(i * i);
        int[] dp = new int[n + 1];
        Arrays.fill(dp, n + 1);
        dp[0] = 0;
        for (int i = 1; i <= n; i++)
            for (int square: squares)
                if (i >= square)
                    dp[i] = Math.min(dp[i], dp[i - square] + 1);
        return dp[n];
    }
}

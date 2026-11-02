// leetcode.cn/problems/decode-ways/  (91)
// submission 465827629  accepted 2023-09-13  runtime 0 ms  memory 39.7 MB

class Solution {
    public int numDecodings(String s) {
        if (s.charAt(0) == '0')
            return 0;
        int n = s.length();
        int[] dp = new int[n + 1];
        dp[0] = 1;
        dp[1] = 1;
        for (int i = 2; i <= n; i++) {
            char ch1 = s.charAt(i - 2);
            char ch2 = s.charAt(i - 1);
            if (ch1 == '1' || (ch1 == '2' && ch2 <= '6'))
                dp[i] += dp[i - 2];
            if (ch2 != '0')
                dp[i] += dp[i - 1];
        }
        return dp[n];
    }
}

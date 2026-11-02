// leetcode.cn/problems/maximum-length-of-repeated-subarray/  (718)
// submission 466296537  accepted 2023-09-14  runtime 21 ms  memory 53.9 MB

class Solution {
    public int findLength(int[] nums1, int[] nums2) {
        int[][] dp = new int[nums1.length + 1][nums2.length + 1];
        for (int i = 0; i <= nums1.length; i++)
            dp[i][0] = 0;
        for (int j = 0; j <=nums2.length; j++)
            dp[0][j] = 0;
        int max = 0;
        for (int i = 1; i <= nums1.length; i++) 
            for (int j = 1; j <= nums2.length; j++) {
                if (nums1[i - 1] == nums2[j - 1])
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                max = Math.max(dp[i][j], max);
            }
        return max;
    }
}

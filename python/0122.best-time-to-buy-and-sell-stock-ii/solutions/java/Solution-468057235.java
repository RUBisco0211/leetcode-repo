// leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/  (122)
// submission 468057235  accepted 2023-09-20  runtime 1 ms  memory 43 MB

class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        for (int i = 0; i < prices.length - 1; i++) {
            if (prices[i + 1] >= prices[i]) {
                profit = profit + prices[i + 1] - prices[i];
            }
        }
        return profit;
    }
}

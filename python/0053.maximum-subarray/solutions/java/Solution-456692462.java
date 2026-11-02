// leetcode.cn/problems/maximum-subarray/  (53)
// submission 456692462  accepted 2023-08-15  runtime 1 ms  memory 56.6 MB

class Solution {
    public int maxSubArray(int[] nums) {
        int sum = 0, max = nums[0];
        for(int i = 0; i < nums.length; i++){
            sum = Math.max(nums[i] + sum, nums[i]);
            max = Math.max(max, sum);
        }
        return max;
    }
}

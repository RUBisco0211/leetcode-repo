// leetcode.cn/problems/move-zeroes/  (283)
// submission 703669396  accepted 2026-03-07  runtime 1 ms  memory 47.1 MB

class Solution {
    public void moveZeroes(int[] nums) {
        if (nums.length == 1) return;
        int slow = 0;
        for (int fast = 0; fast < nums.length; fast++) {
            if (nums[fast] != 0) {
                nums[slow] = nums[fast];
                slow++;
            }
        }
        for (int i = slow; i < nums.length; i++) {
            nums[i] = 0;
        }
    }
}

// leetcode.cn/problems/container-with-most-water/  (11)
// submission 703670601  accepted 2026-03-07  runtime 4 ms  memory 75.8 MB

class Solution {
    public int maxArea(int[] height) {
        int left = 0, right = height.length - 1;
        int max = 0;
        while (left < right) {
            int w = right - left;
            int h = Math.min(height[left], height[right]);
            max = Math.max(max, h * w);
            if (height[left] < height[right])
                left++;
            else
                right--;
        }
        return max;
    }
}

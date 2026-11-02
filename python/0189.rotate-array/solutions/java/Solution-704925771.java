// leetcode.cn/problems/rotate-array/  (189)
// submission 704925771  accepted 2026-03-10  runtime 0 ms  memory 60.1 MB

class Solution {
    public void rotate(int[] nums, int k) {
        if (nums.length <= k) {
            k = k % nums.length;
        }

        flip(nums, 0, nums.length - k);
        flip(nums, nums.length - k, nums.length);
        flip(nums, 0, nums.length);


    }
    public static void flip(int[] arr, int start, int end) {
        for (int i = start; i < (start + end) / 2; i++) {
            int temp = arr[i];
            arr[i] = arr[start + end - i - 1];
            arr[start + end - i - 1] = temp;
        }
    }
}

// leetcode.cn/problems/two-sum/  (1)
// submission 703663858  accepted 2026-03-07  runtime 3 ms  memory 46.3 MB

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int value = target - nums[i];
            if (map.containsKey(value)) {
                return new int[]{map.get(value), i};
            }
            map.put(nums[i], i);
        }
        return null;

    }
}

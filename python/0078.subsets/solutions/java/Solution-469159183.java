// leetcode.cn/problems/subsets/  (78)
// submission 469159183  accepted 2023-09-24  runtime 0 ms  memory 40.3 MB

class Solution {
    private static List<List<Integer>> result;
    public static List<List<Integer>> subsets(int[] nums) {
        result = new ArrayList<>();
        for (int i = 0; i <= nums.length; i++) {
            backTracking(nums, i, 0, new ArrayList<>());
        }
        return result;
    }
    private static void backTracking(int[] nums, int length, int start, List<Integer> combination) {
        if (combination.size() == length) {
            result.add(new ArrayList<>(combination));
            return;
        }
        for (int i = start; i < nums.length; i++) {
            combination.add(nums[i]);
            backTracking(nums, length, i + 1, combination);
            combination.remove(combination.size() - 1);
        }
    }
}

// leetcode.cn/problems/subsets-ii/  (90)
// submission 469166090  accepted 2023-09-24  runtime 2 ms  memory 42.5 MB

class Solution {
    private static Set<List<Integer>> result;
    public static List<List<Integer>> subsetsWithDup(int[] nums) {
        result = new HashSet<>();
        Arrays.sort(nums);
        for (int i = 0; i <= nums.length; i++) {
            backTracking(nums, i, 0, new ArrayList<>());
        }
        return new ArrayList<>(result);
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

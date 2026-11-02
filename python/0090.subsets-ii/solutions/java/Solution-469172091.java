// leetcode.cn/problems/subsets-ii/  (90)
// submission 469172091  accepted 2023-09-24  runtime 1 ms  memory 42.5 MB

class Solution {
    private static List<List<Integer>> result;
    public static List<List<Integer>> subsetsWithDup(int[] nums) {
        result = new ArrayList<>();
        Arrays.sort(nums);
        boolean[] visited = new boolean[nums.length];
        for (int i = 0; i <= nums.length; i++) {
            backTracking(nums, visited, i, 0, new ArrayList<>());
        }
        return result;
    }
    private static void backTracking(int[] nums, boolean[] visited, int length, int start, List<Integer> combination) {
        if (combination.size() == length) {
            result.add(new ArrayList<>(combination));
            return;
        }
        for (int i = start; i < nums.length; i++) {
            if (i > 0 && nums[i - 1] == nums[i] && !visited[i - 1])
                continue;
            visited[i] = true;
            combination.add(nums[i]);
            backTracking(nums, visited, length, i + 1, combination);
            combination.remove(combination.size() - 1);
            visited[i] = false;
        }
    }
}

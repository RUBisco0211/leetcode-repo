// leetcode.cn/problems/permutations-ii/  (47)
// submission 469111388  accepted 2023-09-24  runtime 1 ms  memory 42.6 MB

class Solution {
    private static  List<List<Integer>> result;
    public static List<List<Integer>> permuteUnique(int[] nums) {
        Arrays.sort(nums);
        result = new ArrayList<>();
        boolean[] visited = new boolean[nums.length];
        backTracking(nums, visited, new ArrayList<>());
        return result;
    }
    private static void backTracking(int[] nums, boolean[] visited, List<Integer> list) {
        if (list.size() == nums.length) {
            result.add(new ArrayList<>(list));
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (!visited[i]) {
                if (i > 0 && nums[i] == nums[i - 1] && !visited[i - 1])
                    continue;
                visited[i] = true;
                list.add(nums[i]);
                backTracking(nums, visited, list);
                list.remove(list.size() - 1);
                visited[i] = false;
            }
        }
    }
}

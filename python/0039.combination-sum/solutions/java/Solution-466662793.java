// leetcode.cn/problems/combination-sum/  (39)
// submission 466662793  accepted 2023-09-16  runtime 3 ms  memory 42.7 MB

class Solution {
    private static List<List<Integer>> result;
    public static List<List<Integer>> combinationSum(int[] candidates, int target) {
        result = new ArrayList<>();
        Arrays.sort(candidates);
        backTracking(candidates, 0, 0, target, new ArrayList<>());
        return result;
    }
    private static void backTracking(int[] candidates, int start, int sum, int target, List<Integer> list) {
        if (sum == target) {
            result.add(new ArrayList<>(list));
            return;
        }
        if (sum > target)
            return;

        for (int i = start; i < candidates.length; i++) {
            list.add(candidates[i]);
            backTracking(candidates, i, sum + candidates[i], target, list);
            list.remove(list.size() - 1);
        }
    }
}

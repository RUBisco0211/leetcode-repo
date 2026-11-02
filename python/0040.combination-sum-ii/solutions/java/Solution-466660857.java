// leetcode.cn/problems/combination-sum-ii/  (40)
// submission 466660857  accepted 2023-09-16  runtime 5 ms  memory 41.1 MB

class Solution {
    private static List<List<Integer>> result;
    public static List<List<Integer>> combinationSum2(int[] candidates, int target) {
        result = new ArrayList<>();
        Arrays.sort(candidates);
        backTracking(candidates, 0, target, 0, new ArrayList<>());
        return result;
    }
    private static void backTracking(int[] candidates, int sum, int target, int start, List<Integer> list) {
        if (sum >= target) {
            if (sum == target)
                result.add(new ArrayList<>(list));
            return;
        }
        for (int i = start; i < candidates.length; i++) {
            if (i > start && candidates[i] == candidates[i - 1])
                continue;
            list.add(candidates[i]);
            backTracking(candidates, sum + candidates[i],target, i + 1, list);
            list.remove(list.size() - 1);
        }
    }
}

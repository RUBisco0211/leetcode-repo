// leetcode.cn/problems/combination-sum-iii/  (216)
// submission 466655384  accepted 2023-09-16  runtime 0 ms  memory 38.9 MB

class Solution {
    private static List<List<Integer>> result;
    public static List<List<Integer>> combinationSum3(int k, int n) {
        result = new ArrayList<>();
        backTracking(1, n, k,0, new ArrayList<>());
        return result;
    }
    private static void backTracking(int start, int n, int k, int sum, List<Integer> list){
        if (list.size() == k) {
            if (sum == n)
                result.add(new ArrayList<>(list));
            return;
        }
        for (int i = start; i <= 9; i++) {
            list.add(i);
            backTracking(i + 1, n, k, sum + i, list);
            list.remove(list.size() - 1);
        }

    }
}

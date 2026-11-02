// leetcode.cn/problems/combinations/  (77)
// submission 466648665  accepted 2023-09-16  runtime 15 ms  memory 90.8 MB

class Solution {
    public static void main(String[] args) {
        System.out.println(combine(4, 2));
    }
    private static List<List<Integer>> result;
    public static List<List<Integer>> combine(int n, int k) {
        result = new ArrayList<>();
        backTracking(1, n, k, new ArrayList<>());
        return result;
    }
    private static void backTracking(int start, int n, int k, List<Integer> list){
        if (list.size() == k) {
            result.add(new ArrayList<>(list));
            return;
        }
        for (int i = start; i <= n; i++) {
            list.add(i);
            backTracking(i + 1, n, k, list);
            list.remove(list.size() - 1);
        }

    }
}

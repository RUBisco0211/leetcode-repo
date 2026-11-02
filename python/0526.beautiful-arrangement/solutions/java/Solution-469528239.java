// leetcode.cn/problems/beautiful-arrangement/  (526)
// submission 469528239  accepted 2023-09-25  runtime 49 ms  memory 37.9 MB

class Solution {
    private static int count;
    public static int countArrangement(int n) {
        boolean[] visited = new boolean[n + 1];
        Arrays.fill(visited, false);
        count = 0;
        backTracking(n, 1, visited);
        return count;
    }
    private static void backTracking(int n, int num, boolean[] visited) {
        if (num > n) {
            count++;
            return;
        }
        for (int i = 1; i <= n; i++) {
            if (!visited[i] && (i % num == 0 || num % i == 0)) {
                visited[i] = true;
                backTracking(n, num + 1, visited);
                visited[i] = false;
            }
        }
    }
}

// leetcode.cn/problems/permutation-i-lcci/  (面试题 08.07)
// submission 469239363  accepted 2023-09-24  runtime 8 ms  memory 52.7 MB

class Solution {
    private static List<String> result;
    public static String[] permutation(String S) {
        boolean[] visited = new boolean[S.length()];
        result = new ArrayList<>();
        backTracking(S, visited, new StringBuilder());
        return result.toArray(new String[0]);
    }
    private static void backTracking(String s, boolean[] visited, StringBuilder sb) {
        if (sb.length() == s.length()) {
            result.add(sb.toString());
            return;
        }
        for (int i = 0; i < s.length(); i++) {
            if (!visited[i]) {
                visited[i] = true;
                sb.append(s.charAt(i));
                backTracking(s, visited, sb);
                sb.deleteCharAt(sb.length() - 1);
                visited[i] = false;
            }
        }
    }
}

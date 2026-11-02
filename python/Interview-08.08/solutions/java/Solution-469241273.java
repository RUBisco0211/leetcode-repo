// leetcode.cn/problems/permutation-ii-lcci/  (面试题 08.08)
// submission 469241273  accepted 2023-09-24  runtime 1 ms  memory 42.3 MB

class Solution {
    private static List<String> result;
    public static String[] permutation(String S) {
        char[] sortedCharArray = S.toCharArray();
        Arrays.sort(sortedCharArray);
        String sortedS = new String(sortedCharArray);

        boolean[] visited = new boolean[sortedS.length()];
        result = new ArrayList<>();
        backTracking(sortedS, visited, new StringBuilder());
        return result.toArray(new String[0]);
    }
    private static void backTracking(String s, boolean[] visited, StringBuilder sb) {
        if (sb.length() == s.length()) {
            result.add(sb.toString());
            return;
        }
        for (int i = 0; i < s.length(); i++) {
            if (!visited[i]) {
                if (i > 0 && s.charAt(i - 1) == s.charAt(i) && !visited[i - 1])
                    continue;
                visited[i] = true;
                sb.append(s.charAt(i));
                backTracking(s, visited, sb);
                sb.deleteCharAt(sb.length() - 1);
                visited[i] = false;
            }
        }
    }
}

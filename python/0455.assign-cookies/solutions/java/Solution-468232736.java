// leetcode.cn/problems/assign-cookies/  (455)
// submission 468232736  accepted 2023-09-21  runtime 7 ms  memory 43 MB

class Solution {
    public static int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g);
        Arrays.sort(s);
        int index = s.length - 1;
        int count = 0;
        for (int i = g.length - 1; i >= 0; i--) {
            if (index >= 0 && s[index] >= g[i]) {
                count++;
                index--;
            }
        }
        return count;
    }
}

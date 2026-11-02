// leetcode.cn/problems/longest-substring-without-repeating-characters/  (3)
// submission 703981624  accepted 2026-03-07  runtime 144 ms  memory 46.6 MB

class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() == 0 || s.length() == 1) return s.length();
        int max = 0;

        for (int left = 0; left < s.length() - 1; left++) {
            Set<Character> letters = new HashSet<>();
            letters.add(s.charAt(left));
            int right = left + 1;
            while (right < s.length() && !letters.contains(s.charAt(right))) {
                letters.add(s.charAt(right));
                right++;
            }
            max = Math.max(max, right - left);
        }
        return max;
    }
}

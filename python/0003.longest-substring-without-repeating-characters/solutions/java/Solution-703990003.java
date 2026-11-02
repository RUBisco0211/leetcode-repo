// leetcode.cn/problems/longest-substring-without-repeating-characters/  (3)
// submission 703990003  accepted 2026-03-07  runtime 5 ms  memory 44.8 MB

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int max = 0;
        int left = 0, right = 0;
        Map<Character, Integer> map = new HashMap<>();

        while (right < s.length()) {
            char ch = s.charAt(right);
            if (map.containsKey(ch) && map.get(ch) >= left) {
                left = map.get(ch) + 1;
            }
            map.put(ch, right);
            right++;
            max = Math.max(max, right - left);
        }
        return max;
    }
}

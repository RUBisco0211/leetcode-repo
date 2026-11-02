// leetcode.cn/problems/isomorphic-strings/  (205)
// submission 465290651  accepted 2023-09-11  runtime 12 ms  memory 40.3 MB

class Solution {
    public boolean isIsomorphic(String s, String t) {
        return mapping(s, t) && mapping(t, s);
    }
    private boolean mapping(String s, String t) {
        if (s.length() != t.length())
            return false;
        Map<Character, Character> map = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            if (!map.containsKey(s.charAt(i)))
                map.put(s.charAt(i), t.charAt(i));
            else
            if (!map.get(s.charAt(i)).equals(t.charAt(i)))
                return false;
        }
        return true;
    }
}

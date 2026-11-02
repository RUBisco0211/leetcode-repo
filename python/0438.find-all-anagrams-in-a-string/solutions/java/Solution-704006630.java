// leetcode.cn/problems/find-all-anagrams-in-a-string/  (438)
// submission 704006630  accepted 2026-03-07  runtime 12 ms  memory 46.2 MB

class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> res = new ArrayList<>();

//        统计 p 字符组成
        int[] pCount = new int[26];
        for (char ch : p.toCharArray())
            pCount[ch - 'a']++;

        int len = p.length();
        int[] sCount = new int[26];

        for (int right = 0; right < s.length(); right++) {
            char ch = s.charAt(right);
            sCount[ch - 'a']++;

            int left = right - p.length() + 1;
            if (left < 0) continue;
            if (Arrays.equals(pCount, sCount))
                res.add(left);
            sCount[s.charAt(left) - 'a']--;
        }
        return res;
    }
}

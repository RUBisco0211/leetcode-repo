// leetcode.cn/problems/valid-anagram/  (242)
// submission 466520819  accepted 2023-09-15  runtime 16 ms  memory 42.6 MB

class Solution {
    public boolean isAnagram( String s, String t ){
        Map<Character, Integer> map = new HashMap<Character, Integer>();
        for(int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            map.put(ch, map.getOrDefault(ch, 0) + 1);
        }
        for(int i = 0; i< t.length(); i++){
            char ch = t.charAt(i);
            if(!map.containsKey(ch))
                return false;
            int count = map.get(ch);
            map.put(ch, count - 1);
            if(count - 1 == 0)
                map.remove(ch);
        }
        return map.size() == 0 ;
    }
}

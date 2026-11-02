// leetcode.cn/problems/group-anagrams/  (49)
// submission 458179154  accepted 2023-08-20  runtime 7 ms  memory 45.9 MB

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<String, List<String>>();
        for( String str: strs ) {
            char[] chr = str.toCharArray();
            Arrays.sort( chr );
            String s = new String( chr );
            List<String> list = map.getOrDefault( s, new ArrayList<>() );
            list.add( str );
            map.put( s, list );
        }
        return new ArrayList<List<String>>( map.values() );
    }
}

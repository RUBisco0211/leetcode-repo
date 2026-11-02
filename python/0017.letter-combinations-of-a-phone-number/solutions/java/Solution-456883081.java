// leetcode.cn/problems/letter-combinations-of-a-phone-number/  (17)
// submission 456883081  accepted 2023-08-16  runtime 0 ms  memory 40.2 MB

class Solution {
    private static Map<Character, String> letters;
    private static List<String> result;
    private static StringBuilder sb;

    private static void init() {
        letters = new HashMap<>();
        letters.put( '2', "abc" );
        letters.put( '3', "def" );
        letters.put( '4', "ghi" );
        letters.put( '5', "jkl" );
        letters.put( '6', "mno" );
        letters.put( '7', "pqrs" );
        letters.put( '8', "tuv" );
        letters.put( '9', "wxyz" );
        result = new ArrayList<>();
        sb = new StringBuilder();
    }
    public static List<String> letterCombinations( String digits ) {
        init();
        if( digits.length() == 0 )
            return result;
        backTracking( digits, 0 );
        return result;
    }
    private static void backTracking( String digits, int depth ) {
        if( depth == digits.length() ) {
            result.add( sb.toString() );
            return;
        }
        String temp = letters.get( digits.charAt(depth) );
        for( int i = 0; i < temp.length(); i++ ) {
            sb.append( temp.charAt(i) );
            backTracking( digits, depth + 1);
            sb.deleteCharAt( depth );
        }
    }
}

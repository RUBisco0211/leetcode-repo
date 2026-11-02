// leetcode.cn/problems/generate-parentheses/  (22)
// submission 457713118  accepted 2023-08-18  runtime 1 ms  memory 40.9 MB

class Solution {
    private static List<String> result;
    public static List<String> generateParenthesis(int n ) {
        result = new ArrayList<>();
        generate( "", n, n);
        return result;
    }
    public static void generate( String s, int remainLeft, int remainRight ) {
        if( remainLeft == 0 && remainRight == 0 ) {
            result.add( s );
            return;
        }
        if( remainLeft == 0 )
            generate( s + ")", remainLeft, remainRight - 1 );
        else if( remainLeft == remainRight )
            generate( s + "(", remainLeft - 1, remainRight);
        else if( remainLeft < remainRight ) {
            generate( s + "(", remainLeft - 1, remainRight );
            generate( s + ")", remainLeft, remainRight - 1);
        }
    }
}

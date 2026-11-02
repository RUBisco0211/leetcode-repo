// leetcode.cn/problems/find-the-losers-of-the-circular-game/  (2682)
// submission 456830875  accepted 2023-08-16  runtime 2 ms  memory 42.4 MB

class Solution {
    public int[] circularGameLosers(int n, int k) {
        boolean[] visited = new boolean[n];
        int index = 0, count = 0;
        while( !visited[index] ) {
            visited[index] = true;
            count++;
            index = ( index + count * k ) % n;
        }
        int[] result = new int[n - count];
        int j = 0;
        for( int i = 0; i < n; i++ ) 
            if( !visited[i] ) 
                result[j++] = i + 1;
        return result;
        
    }
}

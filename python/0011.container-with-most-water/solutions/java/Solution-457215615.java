// leetcode.cn/problems/container-with-most-water/  (11)
// submission 457215615  accepted 2023-08-17  runtime 4 ms  memory 54.6 MB

class Solution {
    public int maxArea(int[] height) {
        int left = 0, right = height.length - 1;
        int result = 0;
        while( left < right ) {
            int area = ( right - left ) * Math.min( height[right], height[left] );
            result = Math.max( result, area );
            if( height[right] >= height[left] )
                left ++;
            else 
                right --;
        }
        return result; 
    }
}

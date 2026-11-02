// leetcode.cn/problems/container-with-most-water/  (11)
// submission 457215449  accepted 2023-08-17  runtime 5 ms  memory 54.3 MB

class Solution {
    public int maxArea(int[] height) {
        int left = 0, right = height.length - 1;
        int result = 0;
        while( left < right ) {
            result = Math.max( result, ( right - left ) * Math.min( height[right], height[left] ) );
            if( height[right] >= height[left] )
                left ++;
            else 
                right --;
        }
        return result; 
    }
}

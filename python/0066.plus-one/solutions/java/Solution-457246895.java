// leetcode.cn/problems/plus-one/  (66)
// submission 457246895  accepted 2023-08-17  runtime 0 ms  memory 39.9 MB

class Solution {
    public int[] plusOne(int[] digits) {
        for( int i = digits.length - 1; i >= 0; i-- ) {
            if( digits[i] != 9 ) {
                digits[i] += 1;
                return digits;
            }
            digits[i] = 0;
        }
        int[] temp = new int[digits.length + 1];
        temp[0] = 1;
        return temp; 
    }
    
}

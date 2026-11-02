// leetcode.cn/problems/integer-to-roman/  (12)
// submission 456396573  accepted 2023-08-14  runtime 3 ms  memory 41.8 MB

class Solution {
    public String intToRoman(int num) {
        int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] roman = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < values.length; i++){
            while(num >= values[i]){
                sb.append(roman[i]);
                num -= values[i];
            }
        }

        return sb.toString();
    }
}

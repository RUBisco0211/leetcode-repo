// leetcode.cn/problems/zigzag-conversion/  (6)
// submission 456501835  accepted 2023-08-15  runtime 4 ms  memory 43.3 MB

class Solution {
    public String convert(String s, int numRows) {
        if(numRows == 1)
            return s;
       StringBuilder sb = new StringBuilder();

        int[] sign = new int[s.length()];
        sign[0] = 0;
        int increment = 1;

        for(int i = 0; i < s.length() - 1; i++){
            if(sign[i] == numRows - 1)
                increment = -1;
            if(sign[i] == 0)
                increment = 1;
            sign[i+1] = sign[i] + increment;
        }
        StringBuilder[] temp = new StringBuilder[numRows];
        for(int i = 0; i < numRows; i++)
            temp[i] = new StringBuilder();
        for(int i = 0; i < s.length(); i++)
            temp[sign[i]].append(s.charAt(i));
        for(int i = 0; i < numRows; i++)
            sb.append(temp[i]);
        return sb.toString();
       
    }
}

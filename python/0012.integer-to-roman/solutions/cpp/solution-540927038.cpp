// leetcode.cn/problems/integer-to-roman/  (12)
// submission 540927038  accepted 2024-06-20  runtime 3 ms  memory 12.4 MB

class Solution {
public:
    string intToRoman(int num) {
            vector<int> values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
            vector<string> roman = {"M", "CM", "D" , "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
            string s = "";
            for (int i = 0; i < values.size(); i++) {
                while(num >= values[i]) {
                    s += roman[i];
                    num -= values[i];
                }
            }
            return s;
        }
};

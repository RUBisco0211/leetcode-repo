// leetcode.cn/problems/reverse-string/  (344)
// submission 544415376  accepted 2024-07-06  runtime 11 ms  memory 26.4 MB

class Solution
{
public:
    void reverseString(std::vector<char> &s)
    {
        int n = s.size();
        for (int i = 0; i < n - i - 1; i++)
        {
            char temp = s[i];
            s[i] = s[n - i - 1];
            s[n - i - 1] = temp;
        }
    }
};

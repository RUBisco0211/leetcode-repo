// leetcode.cn/problems/reverse-string/  (344)
// submission 544416380  accepted 2024-07-06  runtime 30 ms  memory 26.3 MB

class Solution
{
public:
    void reverseString(std::vector<char> &s)
    {
        recursion(s, 0, s.size() - 1);
    }
    void recursion(std::vector<char> &s, int left, int right)
    {
        if (left >= right)
            return;
        char temp = s[left];
        s[left] = s[right];
        s[right] = temp;
        recursion(s, left + 1, right - 1);
    }
};

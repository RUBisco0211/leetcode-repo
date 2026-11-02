// leetcode.cn/problems/remove-all-adjacent-duplicates-in-string/  (1047)
// submission 544675379  accepted 2024-07-07  runtime 26 ms  memory 13.1 MB

class Solution {
public:
    std::string removeDuplicates(std::string s)
    {
        std::stack<char> st;
        for (const char &ch : s)
        {
            if (!st.empty() && st.top() == ch)
            {
                st.pop();
            }
            else
            {
                st.push(ch);
            }
        }
        std::stack<char> temp;
        while (!st.empty())
        {
            char top = st.top();
            st.pop();
            temp.push(top);
        }
        std::string res;
        while (!temp.empty())
        {
            res += temp.top();
            temp.pop();
        }
        return res;
    }
};

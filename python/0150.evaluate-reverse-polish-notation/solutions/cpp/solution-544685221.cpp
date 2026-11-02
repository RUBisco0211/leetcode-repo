// leetcode.cn/problems/evaluate-reverse-polish-notation/  (150)
// submission 544685221  accepted 2024-07-07  runtime 11 ms  memory 15.2 MB

#include <iostream>
#include <vector>
#include <string>
#include <stack>

class Solution
{
public:
    int evalRPN(std::vector<std::string> &tokens)
    {
        std::stack<int> st;
        for (const std::string &token : tokens)
        {
            if (!isOperator(token))
                st.push(string2int(token));
            else
            {
                int num2 = st.top();
                st.pop();
                int num1 = st.top();
                st.pop();

                int res;
                switch (token[0])
                {
                case '+':
                    res = num1 + num2;
                    break;
                case '-':
                    res = num1 - num2;
                    break;
                case '*':
                    res = num1 * num2;
                    break;
                case '/':
                    res = num1 / num2;
                    break;
                }
                st.push(res);
            }
        }
        return st.top();
    }

    int string2int(std::string s)
    {
        int factor = 1;
        int res = 0;
        if (s[0] == '-')
        {
            factor = -1;
            s = s.substr(1, s.size() - 1);
        }
        for (const char &ch : s)
        {
            res *= 10;
            res += (ch - '0');
        }
        return factor * res;
    }
    bool isOperator(std::string s)
    {
        if (s.length() != 1)
            return false;
        switch (s[0])
        {
        case '+':
        case '-':
        case '*':
        case '/':
            return true;
        default:
            return false;
        }
    }
};

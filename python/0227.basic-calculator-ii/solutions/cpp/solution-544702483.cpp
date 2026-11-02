// leetcode.cn/problems/basic-calculator-ii/  (227)
// submission 544702483  accepted 2024-07-07  runtime 15 ms  memory 13.3 MB

// 227 基本计算器2
// 无括号，整数均为非负整数
#include <iostream>
#include <string>
#include <stack>

class Solution
{
public:
    int calculate(std::string s)
    {
        std::stack<int> st;
        char pre_operator = '+';
        int num = 0;
        for (int i = 0; i < s.length(); i++)
        {
            const char ch = s[i];
            // 为数字
            if (isdigit(ch))
            {
                // 对数字字符串求和得出对应的值
                num *= 10;
                num += (ch - '0');
            }
            // 为操作符 或 为字符串最后一位 的情况，说明前面的一个数已经求出
            // 根据pre_oper的值确定对栈顶元素的操作
            if (!isdigit(ch) && ch != ' ' || i == s.length() - 1)
            {
                switch (pre_operator)
                {
                case '+':
                    // 加号直接入栈
                    st.push(num);
                    break;
                case '-':
                    // 负号入栈相反数
                    st.push(-num);
                    break;
                case '*':
                {
                    // 乘法在这一步就运算
                    int top = st.top();
                    st.pop();
                    st.push(top * num);
                    break;
                }
                case '/':
                {
                    // 除法在这一步就运算
                    int top = st.top();
                    st.pop();
                    st.push(top / num);
                    break;
                }
                }
                // 更新pre_oper为当前操作符，重置num
                pre_operator = ch;

                // num清零的时机：遇到操作符或遍历到最后一个数字
                num = 0;
            }
            // 为空格的情况不用做额外操作，直接跳过
        }
        // 对栈中数求和即为结果
        int sum = 0;
        while (!st.empty())
        {
            sum += st.top();
            st.pop();
        }
        return sum;
    }
};

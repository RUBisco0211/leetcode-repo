// leetcode.cn/problems/reverse-words-in-a-string/  (151)
// submission 544532891  accepted 2024-07-06  runtime 3 ms  memory 9.2 MB

class Solution
{
public:
    std::string reverseWords(std::string s)
    {
        std::stack<std::string> word_stack;
        std::string temp = "";
        for (char ch : s)
        {
            if (ch == ' ')
            {
                if (temp != "")
                {
                    word_stack.push(temp);
                    temp = "";
                }
                continue;
            }
            else
                temp += ch;
        }
        if (temp != "")
            word_stack.push(temp);

        std::string res;
        while (!word_stack.empty())
        {
            res += word_stack.top();
            word_stack.pop();
            if (word_stack.size() != 0)
                res += ' ';
        }
        return res;
    }
};

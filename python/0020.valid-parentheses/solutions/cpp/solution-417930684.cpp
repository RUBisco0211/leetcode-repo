// leetcode.cn/problems/valid-parentheses/  (20)
// submission 417930684  accepted 2023-03-26  runtime 0 ms  memory 6.2 MB

class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        for(int i=0;i<s.length();i++){
            if(s[i]=='('||s[i]=='{'||s[i]=='[')
                st.push(s[i]);
            else if(s[i]==')'||s[i]=='}'||s[i]==']'){
                if(st.empty())
                    return false;
                char c = st.top();
                if((c=='('&&s[i]==')')||(c=='{'&&s[i]=='}')||(c=='['&&s[i]==']')){
                    st.pop();
                }
                else
                    return false;
            }
        }
        return st.empty();            
    }
};

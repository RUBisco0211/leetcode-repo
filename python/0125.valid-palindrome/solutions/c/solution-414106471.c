// leetcode.cn/problems/valid-palindrome/  (125)
// submission 414106471  accepted 2023-03-16  runtime 192 ms  memory 6.1 MB

bool isPalindrome(char * s){
    int count = 0;
    if(strlen(s) == 0||strlen(s) == 1)
    return true;
    for(int i=0;i<strlen(s);i++){
        if(s[i]>='A'&&s[i]<='Z')
        s[i]+=32;
        if(!((s[i]>='a'&&s[i]<='z') || (s[i]>='0'&&s[i]<='9')))
        count++;
    }
    if(count == strlen(s))
    return true;
    int left = 0, right = strlen(s) - 1;
    while(left<=right){
        while (!((s[left]>='a'&&s[left]<='z') || (s[left]>='0'&&s[left]<='9'))){
            left++;
        }
        while (!((s[right]>='a'&&s[right]<='z') || (s[right]>='0'&&s[right]<='9'))){
            right--;
        }
        if(s[left]!=s[right])
        return false;
        left++;
        right--;
    }
    return true;
}

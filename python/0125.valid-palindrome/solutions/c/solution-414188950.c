// leetcode.cn/problems/valid-palindrome/  (125)
// submission 414188950  accepted 2023-03-16  runtime 4 ms  memory 6.1 MB

bool isPalindrome(char * s){
    int len = strlen(s);
    int left = 0,right = 0;
    int i = 0,j = 0;
    char* temp = (char*)malloc(sizeof(char)*len);
    for(i=0,j=0;i<len;i++){
        if(s[i]>='a'&&s[i]<='z')
        temp[j++] = s[i];
        if(s[i]>='A'&&s[i]<='Z')
        temp[j++] = s[i] + 32;
        if(s[i]>='0'&&s[i]<='9')
        temp[j++] = s[i];
    }
    right = j - 1;
    while(left<=right){
        if(temp[left]!=temp[right])
        return false;
        left++;
        right--;
    }
    return true;
}

// leetcode.cn/problems/length-of-last-word/  (58)
// submission 411759622  accepted 2023-03-11  runtime 4 ms  memory 5.6 MB

int lengthOfLastWord(char * s){
    int len,count = 0;
    for(int i=strlen(s)-1;i>=0;i--){
        if(s[i]!=' '){
            len = i;
            break;
        }
    }
    for(int i=len;i>=0;i--){
        if(s[i]!=' '){
            count++;
        }
        else
        break;
    }
    return count;
}

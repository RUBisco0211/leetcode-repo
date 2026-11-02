// leetcode.cn/problems/reverse-string/  (344)
// submission 414175349  accepted 2023-03-16  runtime 44 ms  memory 12.3 MB

void reverseString(char* s, int sSize){
    char temp;
    for(int l = 0,r = sSize - 1;l<r;l++,r--){
        temp = s[l];
        s[l] = s[r];
        s[r] = temp;
    }
}

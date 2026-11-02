// leetcode.cn/problems/palindrome-number/  (9)
// submission 411617412  accepted 2023-03-10  runtime 0 ms  memory 5.5 MB

bool isPalindrome(int x){
    int reverseNum = 0;
    if(x < 0 || (x%10==0 && x!=0)){
        return false;
    }
    else{
        while(x > reverseNum){
            reverseNum = 10*reverseNum + x%10;
            x = x/10;
        }
        return x == reverseNum || x == reverseNum/10;
    }
}

// leetcode.cn/problems/climbing-stairs/  (70)
// submission 411773373  accepted 2023-03-11  runtime 0 ms  memory 5.4 MB

int climbStairs(int n){
    int j = 0, k = 0, sum = 1;
    for(int i=1;i<=n;i++){
        j = k;
        k = sum;
        sum = j + k;
    }
    return sum;
}

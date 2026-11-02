// leetcode.cn/problems/climbing-stairs/  (70)
// submission 411775089  accepted 2023-03-11  runtime 0 ms  memory 5.2 MB

int climbStairs(int n){
    int j = 0, k = 0, sum = 1;
    // sum为输出的种类数，sum(1) = 1;sum(2) = 2;有sum(n)=sum(n-1)+sum(n-2)
    for(int i=1;i<=n;i++){
        j = k;
        k = sum;
        sum = j + k;
    }
    return sum;
}

// leetcode.cn/problems/sqrtx/  (69)
// submission 411766674  accepted 2023-03-11  runtime 20 ms  memory 5.3 MB

int mySqrt(int x){
    long int i=0;
    while(i<=x/3){
        if(i*i<=x && (i+1)*(i+1)>x){
            break;
        }
        i++;   
    }
    return i;

}

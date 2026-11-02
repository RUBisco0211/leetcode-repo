// leetcode.cn/problems/sqrtx/  (69)
// submission 411766543  accepted 2023-03-11  runtime 28 ms  memory 5.4 MB

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

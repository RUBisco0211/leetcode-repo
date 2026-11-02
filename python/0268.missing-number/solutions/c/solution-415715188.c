// leetcode.cn/problems/missing-number/  (268)
// submission 415715188  accepted 2023-03-20  runtime 20 ms  memory 6.5 MB

int missingNumber(int* nums, int numsSize){
    int sum = 0,sum1 = 0;
    for(int i=0;i<numsSize;i++){
        sum+=nums[i];
    }
    for(int j=1;j<numsSize+1;j++){
        sum1+=j;
    }
    return sum1-sum;
}

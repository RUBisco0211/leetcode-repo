// leetcode.cn/problems/maximum-average-subarray-i/  (643)
// submission 415679324  accepted 2023-03-20  runtime 164 ms  memory 13.8 MB

double findMaxAverage(int* nums, int numsSize, int k){
    int sum = 0,max = 0;
    for(int i=0;i<k;i++)
        sum += nums[i];
    max = sum;
    for(int i=k;i<numsSize;i++){
        sum = sum + nums[i] - nums[i-k];
        max = max>sum?max:sum;
    }
    return (double)max/k;
}

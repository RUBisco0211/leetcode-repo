// leetcode.cn/problems/maximum-subarray/  (53)
// submission 416140811  accepted 2023-03-21  runtime 104 ms  memory 12 MB

int maxSubArray(int* nums, int numsSize){
    int sum = 0,max = nums[0];
    for(int i=0;i<numsSize;i++){
        sum = fmax(nums[i] + sum, nums[i]);
        max = fmax(max,sum);
    }
    return max;
}

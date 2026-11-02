// leetcode.cn/problems/move-zeroes/  (283)
// submission 414170334  accepted 2023-03-16  runtime 76 ms  memory 14.8 MB

void moveZeroes(int* nums, int numsSize){
    int q = 0;
    for(int p=0;p<numsSize;p++){
        if(nums[p]!=0)
            nums[q++] = nums[p];
    }
    for(int i=q;i<numsSize;i++)
        nums[i] = 0;
}

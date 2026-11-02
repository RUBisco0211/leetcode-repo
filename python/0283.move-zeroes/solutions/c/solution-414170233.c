// leetcode.cn/problems/move-zeroes/  (283)
// submission 414170233  accepted 2023-03-16  runtime 84 ms  memory 14.9 MB

void moveZeroes(int* nums, int numsSize){
    int q = 0;
    for(int p=0;p<numsSize;p++){
        if(nums[p]!=0)
            nums[q++] = nums[p];
    }
    for(int i=q;i<numsSize;i++)
        nums[i] = 0;
}

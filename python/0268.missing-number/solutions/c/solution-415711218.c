// leetcode.cn/problems/missing-number/  (268)
// submission 415711218  accepted 2023-03-20  runtime 1208 ms  memory 6.6 MB

int missingNumber(int* nums, int numsSize){
    int temp;
    for(int i=0;i<=numsSize-2;i++){
        for(int j=0;j<=numsSize-i-2;j++){
            if(nums[j]>nums[j+1]){
                temp = nums[j];
                nums[j] = nums[j+1];
                nums[j+1] = temp;
            }
        }
    }
    int k;
    for(k=0;k<numsSize;k++){
        if(nums[k]!=k)
            break;
    }
    return k;
}

// leetcode.cn/problems/remove-element/  (27)
// submission 411748875  accepted 2023-03-11  runtime 4 ms  memory 6 MB

int removeElement(int* nums, int numsSize, int val){
    int j = 0;
    for(int i=0;i<numsSize;i++){
        if(nums[i]!=val){
            nums[j] = nums[i];
            j++;
        }
    }
    return j;
}

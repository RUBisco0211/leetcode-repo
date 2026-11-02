// leetcode.cn/problems/remove-duplicates-from-sorted-array/  (26)
// submission 411687889  accepted 2023-03-10  runtime 16 ms  memory 7.2 MB

int removeDuplicates(int* nums, int numsSize){
    int i = 0;
    for(int j=0;j<numsSize;j++){
        if(nums[i]!=nums[j]){
            nums[i+1] = nums[j];
            i++;
        }
    }
    return i+1;
}

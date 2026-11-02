// leetcode.cn/problems/remove-duplicates-from-sorted-array/  (26)
// submission 411689277  accepted 2023-03-10  runtime 16 ms  memory 7.3 MB

int removeDuplicates(int* nums, int numsSize){
    int i = 0;
    for(int j=0;j<numsSize;j++){
        if(nums[i]!=nums[j]){
            nums[i+1] = nums[j];
            i++;
            // 找到与nums[i]不同的数后将其复制到nums[i+1]处
        }
    }
    return i+1;
}

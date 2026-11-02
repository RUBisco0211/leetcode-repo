// leetcode.cn/problems/remove-duplicates-from-sorted-array/  (26)
// submission 411689885  accepted 2023-03-10  runtime 12 ms  memory 7.2 MB

int removeDuplicates(int* nums, int numsSize){
    int i = 0;
    for(int j=1;j<numsSize;j++){
        // 从第二位开始遍历数组，寻找与nums[i]不同的数
        if(nums[i]!=nums[j]){
            nums[i+1] = nums[j];
            i++;
            // 找到与nums[i]不同的数后将其复制到nums[i+1]处，i后移一位
        }
    }
    return i+1;
}

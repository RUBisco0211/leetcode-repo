// leetcode.cn/problems/contains-duplicate/  (217)
// submission 415963825  accepted 2023-03-21  runtime 120 ms  memory 14 MB

int cmp(const void*a,const void*b){
    return *(int*)a-*(int*)b;
}
bool containsDuplicate(int* nums, int numsSize){
    int flag = 0;
    qsort(nums,numsSize,sizeof(int),cmp);
    for(int i=0;i<numsSize-1;i++){
        if(nums[i]==nums[i+1]){
            flag = 1;
            break;
        }
    }
    if(flag)
        return true;
    else
        return false;
}

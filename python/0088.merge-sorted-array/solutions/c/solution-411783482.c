// leetcode.cn/problems/merge-sorted-array/  (88)
// submission 411783482  accepted 2023-03-11  runtime 4 ms  memory 6 MB

void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n){
    int temp;
    for(int i=0;i<n;i++){
        nums1[i+m] = nums2[i];
    }
    for(int i=0;i<m+n-1;i++){
        for(int j=0;j<m+n-i-1;j++){
            if(nums1[j]>nums1[j+1]){
                temp = nums1[j+1];
                nums1[j+1] = nums1[j];
                nums1[j] = temp;
            }
        }
    }
}

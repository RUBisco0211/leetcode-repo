// leetcode.cn/problems/find-the-duplicate-number/  (287)
// submission 456549043  accepted 2023-08-15  runtime 4 ms  memory 55.1 MB

class Solution {
    public int findDuplicate(int[] nums) {
        int fast = 0, slow = 0;
        while(true){
            
            fast = nums[fast];
            fast = nums[fast];
            slow = nums[slow];
            if( fast == slow )
                break;
        }
        fast = 0;
        while( fast != slow ){
            fast = nums[fast];
            slow = nums[slow];
        }
        return fast;
    }
}

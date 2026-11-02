// leetcode.cn/problems/binary-search/  (704)
// submission 543598057  accepted 2024-07-02  runtime 24 ms  memory 29.1 MB

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0, right = nums.size();
        while (left < right)
        {
            int mid = (left + right) / 2;
            if (nums[mid] < target)
            {
                left = mid + 1;
            }
            else if (nums[mid] > target)
            {
                right = mid;
            }
            else
            {
                return mid;
            }
            
        }
        return -1;
        }
    
};

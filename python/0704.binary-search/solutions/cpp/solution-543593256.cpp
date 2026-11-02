// leetcode.cn/problems/binary-search/  (704)
// submission 543593256  accepted 2024-07-02  runtime 23 ms  memory 29.2 MB

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0, right = nums.size() - 1;
        while (left <= right)
        {
            int mid = (left + right) / 2;
            if (nums[mid] < target)
            {
                // 已经确定target在mid所指数的右侧，故新区间左边界无须考虑mid位置，left = mid + 1
                left = mid + 1;
            }
            else if (nums[mid] > target)
            {
                // 已经确定target在mid所指数的左侧，故新区间右边界无须考虑mid位置，right = mid - 1
                right = mid - 1;
            }
            else
            {
                return mid;
            }
        }
        return -1;
    }
};

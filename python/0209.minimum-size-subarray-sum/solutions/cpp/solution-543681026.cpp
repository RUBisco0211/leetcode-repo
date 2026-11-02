// leetcode.cn/problems/minimum-size-subarray-sum/  (209)
// submission 543681026  accepted 2024-07-03  runtime 25 ms  memory 29.9 MB

class Solution {
public:
    // 滑动窗口
    int minSubArrayLen(int target, vector<int> &nums)
    {
        int n = nums.size();

        int left = 0, right = 0;

        int min_len = n + 1;
        int sum = 0;

        while (right < n)
        {
            sum += nums[right];
            // 左边界右移直至区间和小于target，即：找到right固定时满足条件的最小长度并更新
            while (sum >= target)
            {
                sum -= nums[left];
                min_len = min(min_len, right - left + 1);
                left++;
            }
            right++;
        }
        return min_len == n + 1 ? 0 : min_len;
    }
};

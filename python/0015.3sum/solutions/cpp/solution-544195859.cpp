// leetcode.cn/problems/3sum/  (15)
// submission 544195859  accepted 2024-07-05  runtime 56 ms  memory 26.6 MB

class Solution {
public:
    std::vector<std::vector<int>> threeSum(std::vector<int> &nums)
    {
        // 升序排序后可以实现去重和双指针控制总和
        std::sort(nums.begin(), nums.end());
        int n = nums.size();
        std::vector<std::vector<int>> res;
        // 固定第一个指针，i需要给left和right腾空间，最大值只能到n-3
        for (int i = 0; i < n - 2; i++)
        {
            if (nums[i] > 0)
                // 排序后的第一个数就大于0，则不可能满足条件
                return res;

            if (i > 0 && nums[i - 1] == nums[i])
                // 对第一个数去重
                continue;
            // 此处去重判断不可用nums[i] == nums[i + 1]
            // left的取值从i + 1开始，跳过当前i会导致left的取值范围遗漏i + 1的情况

            // 双指针，left指向第二个数，right指向第三个数
            // left只能向右移动，right只能向左移动（依靠移动来让三数之和取到目标值）
            int left = i + 1, right = n - 1;
            while (left < right)
            {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum > 0)
                    // 总和大了，让right所指的数减小，right左移
                    right--;
                else if (sum < 0)
                    // 总和小了，让left所指的数增大，left右移
                    left++;
                else
                {
                    // 总和正好为目标值
                    res.push_back({nums[i], nums[left], nums[right]});
                    // 对左右指针指向的数去重
                    while (left < right && nums[left] == nums[left + 1])
                        left++;
                    while (left < right && nums[right] == nums[right - 1])
                        right--;
                    left++;
                    right--;
                }
            }
        }
        return res;
    }
};

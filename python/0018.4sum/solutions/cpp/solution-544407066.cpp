// leetcode.cn/problems/4sum/  (18)
// submission 544407066  accepted 2024-07-06  runtime 10 ms  memory 15.6 MB

class Solution {
public:
    // 注意先剪枝再去重，以免遗漏情况
    std::vector<std::vector<int>> fourSum(std::vector<int> &nums, int target)
    {
        int n = nums.size();
        std::vector<std::vector<int>> res;
        std::sort(nums.begin(), nums.end());

        for (int i = 0; i <= n - 4; i++)
        {
            // 剪枝
            if (nums[i] > 0 && target >= 0 && nums[i] > target)
                 return res;
            // 去重
            if (i > 0 && nums[i] == nums[i - 1])
                continue;

            for (int j = i + 1; j <= n - 3; j++)
            {
                long long sumAB = nums[i] + nums[j];

                // 剪枝
                if (sumAB > 0 && target >= 0 && sumAB > target)
                     return res;

                int left = j + 1, right = n - 1;
                // 剪枝
                if (left < n - 1 && sumAB + nums[left] + nums[left + 1] > target)
                    break;

                // 去重
                if (j > i + 1 && nums[j - 1] == nums[j])
                    continue;

                while (left < right)
                {
                   long long sum = sumAB + nums[left] + nums[right];
                    if (sum > target)
                    {
                        right--;
                    }
                    else if (sum < target)
                    {
                        left++;
                    }
                    else
                    {
                        res.push_back({nums[i], nums[j], nums[left], nums[right]});
                        while (left < right && nums[left] == nums[left + 1])
                        {
                            left++;
                        }
                        while (left < right && nums[right] == nums[right - 1])
                        {
                            right--;
                        }
                        left++;
                        right--;
                    }
                }
            }
        }
        return res;
    }
};

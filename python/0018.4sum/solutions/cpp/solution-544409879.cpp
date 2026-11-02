// leetcode.cn/problems/4sum/  (18)
// submission 544409879  accepted 2024-07-06  runtime 9 ms  memory 15.6 MB

class Solution
{
public:
    std::vector<std::vector<int>> fourSum(std::vector<int> &nums, int target)
    {
        int n = nums.size();
        std::vector<std::vector<int>> res;
        std::sort(nums.begin(), nums.end());

        for (int i = 0; i <= n - 4; i++)
        {

            // 剪枝
            if ((long long)nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target)
                break;
            // i太小，不用考虑其他情况，直接往后找
            if ((long long)nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target)
                continue;

            // 去重
            if (i > 0 && nums[i] == nums[i - 1])
                continue;

            for (int j = i + 1; j <= n - 3; j++)
            {
                long long sumAB = nums[i] + nums[j];

                // 剪枝
                if (sumAB + nums[j + 1] + nums[j + 2] > target)
                    break;
                // j太小，不用考虑其他情况，直接往后找
                if (sumAB + nums[n - 2] + nums[n - 1] < target)
                    continue;

                // 去重
                if (j > i + 1 && nums[j - 1] == nums[j])
                    continue;

                int left = j + 1, right = n - 1;
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

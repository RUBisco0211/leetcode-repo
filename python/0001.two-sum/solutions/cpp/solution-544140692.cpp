// leetcode.cn/problems/two-sum/  (1)
// submission 544140692  accepted 2024-07-05  runtime 149 ms  memory 12.4 MB

class Solution {
public:
    std::vector<int> twoSum(std::vector<int> &nums, int target)
    {
        std::vector<int> indexes;
        int n = nums.size();
        for (int i = 0; i < n - 1; i++)
        {
            for (int j = i + 1; j < n; j++)
            {
                if (nums[i] + nums[j] == target)
                {
                    indexes.push_back(i);
                    indexes.push_back(j);
                    return indexes;
                }
            }
        }
        return indexes;
    }
};

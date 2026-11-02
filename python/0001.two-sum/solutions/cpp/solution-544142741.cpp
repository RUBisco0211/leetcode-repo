// leetcode.cn/problems/two-sum/  (1)
// submission 544142741  accepted 2024-07-05  runtime 6 ms  memory 13.8 MB

class Solution {
public:
    std::vector<int> twoSum(std::vector<int> &nums, int target)
    {
        std::unordered_map<int, int> map;
        for (int i = 0; i < nums.size(); i++)
        {
            auto it = map.find(target - nums[i]);
            if (it != map.end())
                // 存在target - nums[i]
                return {i, it->second};
            // 先检查是否已经有target - nums[i]，再插入当前项，确保当前数不会与自身匹配
            map[nums[i]] = i;
        }
        return {};
    }
};

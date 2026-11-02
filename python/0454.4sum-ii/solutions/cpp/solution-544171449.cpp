// leetcode.cn/problems/4sum-ii/  (454)
// submission 544171449  accepted 2024-07-05  runtime 182 ms  memory 27.5 MB

class Solution {
public:
    int fourSumCount(std::vector<int> &nums1, std::vector<int> &nums2, std::vector<int> &nums3, std::vector<int> &nums4)
    {
        std::unordered_map<int, int> map;
        int sum = 0;
        for (int i : nums1)
        {
            for (int j : nums2)
            {
                map[i + j]++;
            }
        }
        for (int k : nums3)
        {
            for (int l : nums4)
            {
                if (map.count(-k - l))
                {
                    sum += map[-k - l];
                }
            }
        }
        return sum;
    }
};

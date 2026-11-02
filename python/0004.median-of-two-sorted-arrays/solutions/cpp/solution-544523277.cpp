// leetcode.cn/problems/median-of-two-sorted-arrays/  (4)
// submission 544523277  accepted 2024-07-06  runtime 37 ms  memory 93 MB

    class Solution {
    public:
        // O(m + n) 合并之后找中位数
    double findMedianSortedArrays(std::vector<int> &nums1, std::vector<int> &nums2)
    {
        int m = nums1.size(), n = nums2.size();
        std::vector<int> merged_arr;
        int i = 0, j = 0;
        while (i < m && j < n)
        {
            if (nums1[i] <= nums2[j])
            {
                merged_arr.push_back(nums1[i]);
                i++;
            }
            else
            {
                merged_arr.push_back(nums2[j]);
                j++;
            }
        }
        if (i == m)
        {
            while (j < n)
            {
                merged_arr.push_back(nums2[j]);
                j++;
            }
        }
        if (j == n)
        {
            while (i < m)
            {
                merged_arr.push_back(nums1[i]);
                i++;
            }
        }
        if ((m + n) % 2)
            return (double)merged_arr[(m + n) / 2];
        return (double)(merged_arr[(m + n) / 2 - 1] + merged_arr[(m + n) / 2]) / 2;
    }
    };

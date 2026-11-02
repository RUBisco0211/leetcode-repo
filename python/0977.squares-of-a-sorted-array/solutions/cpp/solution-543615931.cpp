// leetcode.cn/problems/squares-of-a-sorted-array/  (977)
// submission 543615931  accepted 2024-07-02  runtime 8 ms  memory 28.9 MB

class Solution
{
public:
    vector<int> sortedSquares(vector<int> &nums)
    {
        int n = nums.size();

        if (n == 1)
        {
            vector<int> squares;
            squares.push_back(nums[0] * nums[0]);
            return squares;
        }

        int sep = -1;
        // 找到单调不递减数组中的最后一个负数
        for (int i = 0; i < n; i++)
        {
            if (nums[i] < 0)
            {
                sep = i;
            }
            else
            {
                break;
            }
        }

        vector<int> squares;

        int left = sep, right = sep + 1;
        while (left >= 0 && right < n)
        {
            int lsq = nums[left] * nums[left], rsq = nums[right] * nums[right];
            if (lsq <= rsq)
            {
                squares.push_back(lsq);
                left--;
            }
            else
            {
                squares.push_back(rsq);
                right++;
            }
        }
        if (left < 0)
        {
            while (right < n)
            {
                squares.push_back(nums[right] * nums[right]);
                right++;
            }
        }
        else
        {
            while (left >= 0)
            {
                squares.push_back(nums[left] * nums[left]);
                left--;
            }
        }
        return squares;
    }
};

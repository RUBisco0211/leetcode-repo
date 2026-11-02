// leetcode.cn/problems/remove-element/  (27)
// submission 543603851  accepted 2024-07-02  runtime 4 ms  memory 10.2 MB

class Solution
{
public:
    int removeElement(vector<int> &nums, int val)
    {
        // 双指针，i指向需要当前处理的数，j指向数组中下一个可用的赋值位置
        int j = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] != val)
            {
                // i指向的数不为val，复制到j所在位置，j后移一位
                nums[j] = nums[i];
                j++;
            }
        }
        return j;
    }
};

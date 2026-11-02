// leetcode.cn/problems/happy-number/  (202)
// submission 544139101  accepted 2024-07-05  runtime 7 ms  memory 7.8 MB

class Solution {
public:
        bool isHappy(int n)
    {
        std::unordered_set<int> set;
        int num = n;
        set.insert(num);
        while (1)
        {
            num = digitSquareSum(num);
            if (num == 1)
                return true;
            auto it = set.find(num);
            if (it != set.end())
                // 已存在，不为快乐数
                return false;
            // 不存在，加入
            set.insert(num);
        }
    }
    int digitSquareSum(int n)
    {
        int sum = 0;
        int num = n;
        while (num != 0)
        {
            int d = num % 10;
            sum += (d * d);
            num = num / 10;
        }
        return sum;
    }
};

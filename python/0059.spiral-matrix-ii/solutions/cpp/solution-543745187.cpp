// leetcode.cn/problems/spiral-matrix-ii/  (59)
// submission 543745187  accepted 2024-07-03  runtime 0 ms  memory 7.7 MB

class Solution
{
public:
    std::vector<std::vector<int>> generateMatrix(int n)
    {
        int left = 0, right = n - 1, top = 0, bottom = n - 1;
        // left指向已经填充的列的后一列
        // right指向已经填充的列的前一列
        // top指向已经填充的行的下一行
        // bottom指向已经填充的行的上一行

        // 记得初始化vector
        std::vector<std::vector<int>> mat(n, std::vector<int>(n));
        int num = 1, target = n * n;
        // 循环条件若为 left < right || top < bottom，n为奇数时中心位置的数无法被填充（中心位置left == right，top == bottom）
        // 但如果取等，n为偶数时会覆盖已填充的行或列
        while (num <= target)
        {
            for (int i = left; i <= right; i++)
            {
                mat[top][i] = num;
                num++;
            }
            top++;
            for (int i = top; i <= bottom; i++)
            {
                mat[i][right] = num;
                num++;
            }
            right--;
            for (int i = right; i >= left; i--)
            {
                mat[bottom][i] = num;
                num++;
            }
            bottom--;
            for (int i = bottom; i >= top; i--)
            {
                mat[i][left] = num;
                num++;
            }
            left++;
        }
        return mat;
    }
};

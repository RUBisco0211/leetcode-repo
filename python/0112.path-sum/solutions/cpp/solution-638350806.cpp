// leetcode.cn/problems/path-sum/  (112)
// submission 638350806  accepted 2025-06-22  runtime 0 ms  memory 21.1 MB

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
#include <vector>
#include <algorithm>

using namespace std;
// struct TreeNode
// {
//     int val;
//     TreeNode *left;
//     TreeNode *right;
//     TreeNode() : val(0), left(nullptr), right(nullptr) {}
//     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
//     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
// };

class Solution
{
private:
    vector<int> sums;

public:
    bool hasPathSum(TreeNode *root, int targetSum)
    {
        if (root == nullptr)
            return false;
        backTracking(root, 0);
        return std::find(sums.begin(), sums.end(), targetSum) != sums.end();
    }
    void backTracking(TreeNode *root, int sum)
    {
        if (root == nullptr)
            return;
        if (root->left == nullptr && root->right == nullptr)
        {
            sums.push_back(sum + root->val);
            return;
        }
        if (root->left != nullptr)
            backTracking(root->left, sum + root->val);
        if (root->right != nullptr)
            backTracking(root->right, sum + root->val);
    }
};

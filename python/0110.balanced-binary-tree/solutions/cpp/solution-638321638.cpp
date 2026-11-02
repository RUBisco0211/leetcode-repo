// leetcode.cn/problems/balanced-binary-tree/  (110)
// submission 638321638  accepted 2025-06-22  runtime 0 ms  memory 22.6 MB

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
#include <math.h>
#include <algorithm>
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
public:
    bool isBalanced(TreeNode *root)
    {
        if (root == nullptr)
            return true;
        return isBalanced(root->left) && isBalanced(root->right) && std::abs(depth(root->left) - depth(root->right)) <= 1;
    }
    int depth(TreeNode *root)
    {
        if (root == nullptr)
            return 0;
        int d1 = depth(root->left), d2 = depth(root->right);
        return std::max(d1, d2) + 1;
    }
};

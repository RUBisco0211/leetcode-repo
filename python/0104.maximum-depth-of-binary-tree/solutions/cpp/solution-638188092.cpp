// leetcode.cn/problems/maximum-depth-of-binary-tree/  (104)
// submission 638188092  accepted 2025-06-21  runtime 0 ms  memory 18.6 MB

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
#include <algorithm>
class Solution
{
public:
    int maxDepth(TreeNode *root)
    {
        if (!root)
            return 0;
        int d1 = maxDepth(root->left), d2 = maxDepth(root->right);
        return std::max(d1, d2) + 1;
    }
};

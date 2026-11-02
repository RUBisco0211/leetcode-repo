// leetcode.cn/problems/symmetric-tree/  (101)
// submission 638183934  accepted 2025-06-21  runtime 0 ms  memory 18.2 MB

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
    bool isSymmetric(TreeNode *root)
    {
        if (!root)
            return false;
        if (!root->left && root->right || root->left && !root->right)
            return false;
        if (!root->left && !root->right)
            return true;
        return isReversed(root->left, root->right);
    }
    bool isReversed(TreeNode *node1, TreeNode *node2)
    {
        if (node1 == nullptr && node2 == nullptr)
            return true;
        if (node1 && node2)
            return node1->val == node2->val && isReversed(node1->left, node2->right) && isReversed(node1->right, node2->left);
        return false;
    }
};

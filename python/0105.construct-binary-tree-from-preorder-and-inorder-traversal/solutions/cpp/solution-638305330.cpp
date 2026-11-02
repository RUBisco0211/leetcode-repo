// leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/  (105)
// submission 638305330  accepted 2025-06-22  runtime 31 ms  memory 72.7 MB

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
#include <vector>
#include <algorithm>
using namespace std;
class Solution
{
public:
    TreeNode *buildTree(vector<int> &preorder, vector<int> &inorder)
    {
        if (preorder.size() == 0)
            return nullptr;
        int rootVal = preorder.at(0);
        TreeNode *root = new TreeNode(rootVal);
        auto iter = find(inorder.begin(), inorder.end(), rootVal);

        auto leftInorder = vector<int>(inorder.begin(), iter);
        auto rightInorder = vector<int>(iter + 1, inorder.end());

        auto leftPreorder = vector<int>(preorder.begin() + 1, preorder.begin() + 1 + leftInorder.size());
        auto rightPreorder = vector<int>(preorder.begin() + 1 + leftInorder.size(), preorder.end());

        root->left = buildTree(leftPreorder, leftInorder);
        root->right = buildTree(rightPreorder, rightInorder);
        return root;
    }
};

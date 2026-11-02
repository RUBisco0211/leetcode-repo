// leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/  (106)
// submission 638304760  accepted 2025-06-22  runtime 24 ms  memory 72.8 MB

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
    TreeNode *buildTree(vector<int> &inorder, vector<int> &postorder)
    {
        if (inorder.size() == 0)
            return nullptr;
        int rootVal = postorder.back();
        TreeNode *root = new TreeNode(rootVal);
        auto iter = find(inorder.begin(), inorder.end(), rootVal);

        auto leftInorder = vector<int>(inorder.begin(), iter);
        auto leftPostorder = vector<int>(postorder.begin(), postorder.begin() + leftInorder.size());

        auto rightInorder = vector<int>(iter + 1, inorder.end());
        auto rightPostorder = vector<int>(postorder.begin() + leftPostorder.size(), postorder.end() - 1);

        root->left = buildTree(leftInorder, leftPostorder);
        root->right = buildTree(rightInorder, rightPostorder);
        return root;
    }
};

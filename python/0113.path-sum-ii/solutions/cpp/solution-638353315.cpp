// leetcode.cn/problems/path-sum-ii/  (113)
// submission 638353315  accepted 2025-06-22  runtime 19 ms  memory 34.7 MB

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
#include <numeric>
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
    vector<vector<int>> results;
    int targetSum;

public:
    vector<vector<int>> pathSum(TreeNode *root, int targetSum)
    {
        this->targetSum = targetSum;
        if (root == nullptr)
            return results;
        vector<int> res;
        backTrack(root, res);
        return results;
    }

    void backTrack(TreeNode *node, vector<int> res)
    {
        if (node == nullptr)
            return;
        res.push_back(node->val);
        if (node->left == nullptr && node->right == nullptr)
        {
            int s = 0;
            for (int n : res)
                s += n;
            if (s == targetSum)
                results.push_back(res);
            return;
        }
        if (node->left != nullptr)
            backTrack(node->left, res);
        if (node->right != nullptr)
            backTrack(node->right, res);
    }
};

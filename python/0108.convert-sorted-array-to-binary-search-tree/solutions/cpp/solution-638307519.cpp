// leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/  (108)
// submission 638307519  accepted 2025-06-22  runtime 4 ms  memory 25.6 MB

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
using namespace std;
class Solution
{
public:
    TreeNode *sortedArrayToBST(const vector<int> &nums)
    {
        if (nums.size() == 0)
            return nullptr;
        int m = nums.size() / 2;
        TreeNode *root = new TreeNode(nums.at(m));
        root->left = sortedArrayToBST(vector<int>(nums.begin(), nums.begin() + m));
        root->right = sortedArrayToBST(vector<int>(nums.begin() + m + 1, nums.end()));
        return root;
    }
};

// leetcode.cn/problems/sum-root-to-leaf-numbers/  (129)
// submission 457029754  accepted 2023-08-16  runtime 0 ms  memory 39 MB

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int sum;
    public int sumNumbers(TreeNode root) {
        int num = 0;
        dfs( root, num );
        return sum;
    }
    private void dfs( TreeNode node, int num ) {
        num *= 10;
        num += node.val;
        if( node.left == null && node.right == null ) {
            sum += num;
            return;
        }
        if( node.left != null ) 
            dfs( node.left, num );
        if( node.right != null ) 
            dfs( node.right, num );
    }
}

// leetcode.cn/problems/path-sum-ii/  (113)
// submission 456933422  accepted 2023-08-16  runtime 1 ms  memory 42.9 MB

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
    private List<List<Integer>> result;
    private List<Integer> temp;
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        int sum = 0;
        result = new ArrayList();
        temp = new ArrayList();
        if( root != null )
            dfs( root, sum, targetSum );
        return result;
    }
    public void dfs( TreeNode node, int sum, int targetSum ) {
        temp.add( node.val );
        sum += node.val;
        if( node.left == null && node.right == null ) {
            if( sum == targetSum ) 
                result.add( new ArrayList( temp ) );
            return;
        }
        if( node.left != null ) {
            dfs( node.left, sum, targetSum );
            temp.remove( temp.size() - 1 );
        }
        if( node.right != null ) {
            dfs( node.right, sum, targetSum );
            temp.remove( temp.size() - 1 );
        }
    }
}

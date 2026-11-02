// leetcode.cn/problems/binary-tree-right-side-view/  (199)
// submission 457176915  accepted 2023-08-17  runtime 0 ms  memory 39.9 MB

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
    private List<Integer> result;
    public List<Integer> rightSideView(TreeNode root) {
        result = new ArrayList();
        dfs( root, 0 );
        return result;
    }
    private void dfs( TreeNode node, int depth ) {
        if( node == null )
            return;
        if( result.size() == depth )
            result.add( node.val );
        dfs( node.right, depth + 1 );
        dfs( node.left, depth + 1 );
    } 
}

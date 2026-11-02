// leetcode.cn/problems/flatten-binary-tree-to-linked-list/  (114)
// submission 457108193  accepted 2023-08-16  runtime 1 ms  memory 39.8 MB

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
    private List<TreeNode> list;
    public void flatten(TreeNode root) {
        list = new ArrayList<TreeNode>();
        if( root == null ) 
            return;
        preorderTraverse( root );
        for( int i = 0; i < list.size() - 1; i++ ) {
            list.get( i ).right = list.get( i + 1 );
            list.get( i ).left = null;
        }
        list.get( list.size() - 1 ).right = null;
        list.get( list.size() - 1 ).left = null;
    }
    private void preorderTraverse( TreeNode node ) { 
        if( node == null ) 
            return;
        list.add( node );
        preorderTraverse( node.left ); 
        preorderTraverse( node.right );      
    }
}

// leetcode.cn/problems/recover-binary-search-tree/  (99)
// submission 457083586  accepted 2023-08-16  runtime 1 ms  memory 42.1 MB

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
    public void recoverTree(TreeNode root) {
        list = new ArrayList();
        inorderTraverse( root );

            TreeNode left = null, right = null;
        int i;
        for( i = 0; i < list.size() - 1; i++ ) 
            if( list.get( i ).val >= list.get( i + 1 ).val ) {
                left = list.get( i );
                right = list.get( i + 1 );
                break;
            }
        int j;
        for( j = i + 1; j < list.size() - 1; j++ )
            if( list.get( j ).val >= list.get( j + 1 ).val ) {
                right = list.get( j + 1 );
                break;
            }
        if( left != null && right !=null ) {
             int temp = left.val;
            left.val = right.val;
            right.val = temp;
        }
       
    }
    private void inorderTraverse( TreeNode node ) { 
        if( node.left == null && node.right == null ) {
            list.add( node );
            return;
        }
        if( node.left != null )
            inorderTraverse( node.left );
        list.add( node );
        if( node.right != null )
            inorderTraverse( node.right );      
    }
    
}

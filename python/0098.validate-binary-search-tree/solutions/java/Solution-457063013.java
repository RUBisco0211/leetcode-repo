// leetcode.cn/problems/validate-binary-search-tree/  (98)
// submission 457063013  accepted 2023-08-16  runtime 2 ms  memory 42.6 MB

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
    private List<Integer> list;
    public boolean isValidBST(TreeNode root) {
        list = new ArrayList<Integer>();
        inorderTraverse( root );
        for(int i = 1; i < list.size(); i++) 
            if( list.get( i - 1 ) >= list.get( i ) )
                return false;
        return true;
    }
    private void inorderTraverse( TreeNode node ) { 
        if( node.left == null && node.right == null ) {
            list.add( node.val );
            return;
        }
        if( node.left != null )
            inorderTraverse( node.left );
        list.add( node.val );
        if( node.right != null )
            inorderTraverse( node.right );      
    }
    
}

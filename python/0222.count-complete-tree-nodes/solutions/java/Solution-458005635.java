// leetcode.cn/problems/count-complete-tree-nodes/  (222)
// submission 458005635  accepted 2023-08-19  runtime 5 ms  memory 43.9 MB

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
    public int countNodes(TreeNode root) {
        if( root == null )
            return 0;
        Queue<TreeNode> queue = new LinkedList();
        queue.offer( root );
        int count = 0;

        while( !queue.isEmpty() ) {
            TreeNode node = queue.poll();
            count++;
            if( node.left != null ) 
                queue.offer( node.left );
            if( node.right != null )
                queue.offer( node.right );
        }
        return count;
    }
}

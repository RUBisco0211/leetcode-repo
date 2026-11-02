// leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/  (105)
// submission 459270515  accepted 2023-08-23  runtime 116 ms  memory 78.7 MB

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
var buildTree = function(preorder, inorder) {
    if(!preorder.length || !inorder.length) 
        return null;
    let node = new TreeNode(preorder[0]);
    let index = inorder.indexOf(preorder.shift());

    node.left = buildTree(preorder, inorder.slice(0, index));
    node.right = buildTree(preorder, inorder.slice(index + 1));

    return node;
};

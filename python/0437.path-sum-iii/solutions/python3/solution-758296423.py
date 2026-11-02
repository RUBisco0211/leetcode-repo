# leetcode.cn/problems/path-sum-iii/  (437)
# submission 758296423  accepted 2026-11-02  runtime 546 ms  memory 21.7 MB

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def rootSum(root: Optional[TreeNode], target: int):
            if not root:
                return 0
            _ans = 0

            if root.val == target:
                _ans += 1

            _ans += rootSum(root.left, target - root.val)
            _ans += rootSum(root.right, target - root.val)

            return _ans

        if not root:
            return 0

        ans = rootSum(root, targetSum)

        ans += self.pathSum(root.left, targetSum)
        ans += self.pathSum(root.right, targetSum)
        return ans

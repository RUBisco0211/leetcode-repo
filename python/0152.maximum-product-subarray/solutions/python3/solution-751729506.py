# leetcode.cn/problems/maximum-product-subarray/  (152)
# submission 751729506  accepted 2026-09-27  runtime 7 ms  memory 20.8 MB

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        # 子问题：由于有正负，需要维护 dp_max 和 dp_min
        # dp_max[i] 表示 nums 中以 nums[i] 结尾的乘积最大子数组积
        # dp_min[i] 表示 nums 中以 nums[i] 结尾的乘积最小子数组积


        n = len(nums)
        if n == 1:
            return nums[0]
        
        dp_max = nums.copy()
        dp_min = nums.copy()

        for i in range(1, n):
            x = nums[i]
            dp_max[i] = max(dp_max[i - 1] * x, dp_min[i - 1] * x, x)
            dp_min[i] = min(dp_max[i - 1] * x, dp_min[i - 1] * x, x)
        
        return max(dp_max)

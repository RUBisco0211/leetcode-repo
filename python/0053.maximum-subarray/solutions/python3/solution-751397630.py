# leetcode.cn/problems/maximum-subarray/  (53)
# submission 751397630  accepted 2026-09-25  runtime 44 ms  memory 31 MB

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # dp[i] 表示以 nums[i] 结尾的最大子数组和
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            # 以 nums[i] 结尾，如果前面的子数组和更大，就延续，否则从 nums[i] 开始单起新子数组
            dp[i] = nums[i] + max(dp[i - 1], 0)
        

        return max(dp)

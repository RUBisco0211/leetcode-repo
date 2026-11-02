# leetcode.cn/problems/house-robber/  (198)
# submission 751690289  accepted 2026-09-27  runtime 0 ms  memory 19.1 MB

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)

        # 子问题定义：dp[i] 为从前 i 间房中偷，能偷到的最多钱
        # 两种情况：i 不偷，则 dp[i] = dp[i - 1]
        # i 偷，则 dp[i] = nums[i] + dp[i - 2]
        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[:2])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        
        return max(dp)

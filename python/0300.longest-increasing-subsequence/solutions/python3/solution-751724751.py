# leetcode.cn/problems/longest-increasing-subsequence/  (300)
# submission 751724751  accepted 2026-09-27  runtime 1360 ms  memory 19.1 MB

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # 子问题：nums[0:i + 1] 中，以 nums[i] 结尾的最长递增子序列
        # 则要再遍历 j in range(i):
        # nums[j] < nums[i] 时，j -> i 存在以 nums[i] 结尾的递增子序列，需要取更新最大值
        # 最后取 max[dp]
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)

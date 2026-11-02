# leetcode.cn/problems/subarray-sum-equals-k/  (560)
# submission 751378835  accepted 2026-09-25  runtime 39 ms  memory 21.6 MB

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        l = len(nums)
        if l == 0:
            return 0
        if l == 1:
            return (1 if nums[0] == k else 0)

        res = 0
        pre = 0 # 保存 sum(num[0: i + 1])，即前缀和
        # mp[sum] = count，保存前缀和为 sum 的子串数量
        # 初始 {0: 1} 是为了前缀和为 k 时，即 pre - k == 0 时
        mp = {
            # 0: 1
        }

        for i, n in enumerate(nums):
            pre += n
            if pre == k:
                res += 1
            # 前缀和 pre - k 已经出现过了，说明存在子串 nums[j: i + 1] 和为 k，数量就是不同 j 的个数
            if pre - k in mp:
                res += mp[pre - k]
            # 更新当前的前缀和 pre 的出现次数
            mp[pre] = mp[pre] + 1 if pre in mp else 1


        return res
